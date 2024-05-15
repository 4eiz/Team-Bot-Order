from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from keyboards.client import worker_menu, Menu_callback, send_request, worker_menu_admin
from data import users

from config import ADMIN, bot

router = Router()




@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    try:
        await state.clear()
    except:
        pass

    id = message.from_user.id
    start_user = await users.check_worker_in_database(id)
    if start_user == True:
        text = f'''<b>
👋 Здравствуйте, <code>{message.from_user.first_name}</code>!

💎Добро пожаловать в Fortune Team!💎

🔱у нас лучшие офферы по OnlyFans:
—————————————————————
└ Платный подписчик от 5$ 
└ Бесплатный подписчик от 0.5$
└ Индивидуальные предложения

⚡️Перед началом работы:
—————————————————————
└ Запросите индивидуальную ссылку
└ Ознакомитесь с функционалом
└ Подайте заявку в филиал 
└ Прочитайте инструкции
</b>'''
        if id in ADMIN:
            kb = worker_menu_admin()
        else:
            kb = worker_menu()

        await message.answer(text, reply_markup=kb)

    else:
        text = f'<b>👋 Здравствуйте, {message.from_user.first_name}!\n\nЗаполните заявку по кнопке ниже.</b>'
        await message.answer(text, reply_markup=send_request())



@router.callback_query(Menu_callback.filter(F.menu == 'menu'))
async def start(call: CallbackQuery, callback_data: Menu_callback, state: FSMContext):
    try:
        await state.clear()
    except:
        pass

    id = call.from_user.id
    start_user = await users.check_worker_in_database(id)
    if start_user == True:
        text = f'''<b>
👋 Здравствуйте, <code>{call.from_user.first_name}</code>!

💎Добро пожаловать в Fortune Team!💎

🔱у нас лучшие офферы по OnlyFans:
—————————————————————
└ Платный подписчик от 5$ 
└ Бесплатный подписчик от 0.5$
└ Индивидуальные предложения

⚡️Перед началом работы:
—————————————————————
└ Запросите индивидуальную ссылку
└ Ознакомитесь с функционалом
└ Подайте заявку в филиал 
└ Прочитайте инструкции
</b>'''
        if id in ADMIN:
            kb = worker_menu_admin()
        else:
            kb = worker_menu()

        await call.message.edit_text(text, reply_markup=kb)

    else:
        text = f'<b>👋 Здравствуйте, <code>{call.from_user.first_name}</code>!\n\nЗаполните заявку по кнопке ниже.</b>'
        await call.message.edit_text(text, reply_markup=send_request())



    # if message.from_user.id == ADMIN:
    #     await message.answer(f'<b>👋 Здравствуйте, {message.from_user.first_name}!\n\n'
    #                         'Вы сейчас находитесь в главном меню.</b>', reply_markup=k_menu2())
    # else:
    #     await message.answer(f'<b>👋 Здравствуйте, {message.from_user.first_name}!\n\n'
    #                         'Вы сейчас находитесь в главном меню.</b>', reply_markup=k_menu())

