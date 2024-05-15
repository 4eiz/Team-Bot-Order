from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.client import Answer_callback, accept, decline, worker_menu, send_request, Menu_callback, admin_panel, offers_cancel, worker_menu_admin
from data.requests import delete_req
from data.users import new_user
from data.admin import update_offers
from config import bot


router = Router()


class Update(StatesGroup):
    new_text = State()




@router.callback_query(Answer_callback.filter(F.answer == 'accept'))
async def accept_form(call: CallbackQuery, callback_data: Answer_callback, state: FSMContext):

    user_id = callback_data.user_id
    text1 = '<b>Ваша заявка была одобрена</b>'
    await call.message.edit_reply_markup(reply_markup=accept())
    await bot.send_message(chat_id=user_id, text=text1)
    await delete_req(user_id)
    await new_user(user_id)

    text2 = f'''<b>
👋 Здравствуйте!

💎Добро пожаловать в Fortune Team!💎

🔱У нас лучшие офферы по OnlyFans:
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

    await bot.send_message(chat_id=user_id, text=text2, reply_markup=worker_menu())


@router.callback_query(Answer_callback.filter(F.answer == 'decline'))
async def decline_form(call: CallbackQuery, callback_data: Answer_callback, state: FSMContext):
    user_id = callback_data.user_id
    text = '<b>Вашу заявку отклонили, попробуйте заполнить анкету заново</b>'
    await delete_req(user_id)
    await call.message.edit_reply_markup(reply_markup=decline())
    await bot.send_message(chat_id=user_id, text=text, reply_markup=send_request())



@router.callback_query(Menu_callback.filter(F.menu == 'admin_menu'))
async def admin(call: CallbackQuery, callback_data: Menu_callback):
    text = '<b>Админ панель</b>'
    await call.message.edit_text(text=text, reply_markup=admin_panel())


@router.callback_query(Menu_callback.filter(F.menu == 'change_offers'))
async def change_offers1(call: CallbackQuery, callback_data: Menu_callback, state: FSMContext):
    # print('Тут')
    try:
        await state.clear()
    except:
        pass
    
    text = '<b>Введите новое <code>актуальное</code></b>'
    await call.message.edit_text(text=text, reply_markup=offers_cancel())
    await state.set_state(Update.new_text)


@router.message(Update.new_text)
async def change_offers2(message: Message, state: FSMContext):
    text = message.text
    await update_offers(text=text)
    text_answer = '<b>Актуальное успешно изменено.</b>'
    await message.answer(text=text_answer, reply_markup=worker_menu_admin())
    await state.clear()