from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.client import Menu_callback, send_req_branches, menu, admin_conf_branches, fillial_kb
from config import bot, CHANNEL_ID
from data import requests
from data.fillials import get_fillial_info

router = Router()


class Branches_req(StatesGroup):
    question1 = State()




@router.callback_query(Menu_callback.filter(F.menu == 'branches'))
async def start_form(call: CallbackQuery, callback_data: Menu_callback):
    user_id = call.from_user.id
    data = await get_fillial_info(user_id=user_id)
    if not data:
        text = '''<b>
🙋‍♂️Подача заявки в филиал 🙋‍♂️
—————————————————————
📣Подайте заявку если вы:
└ Ознакомились с ботом
└ Внимательно изучили инструкции 
└ Запросили индивидуальную ссылку
└ Создали аккаунт Instagram под модель
</b>'''
        kb = send_req_branches()

    else:
        text = '''<b>
Текст филлалов
</b>'''
        url = data[1]
        kb = fillial_kb(url=url)

    await call.message.edit_text(text=text, reply_markup=kb)


@router.callback_query(Menu_callback.filter(F.menu == 'send_req_branches'))
async def start_form(call: CallbackQuery, callback_data: Menu_callback, state: FSMContext):
    await state.set_state(Branches_req.question1)
    text = 'Отправьте ссылку на инстаграм'
    await call.message.edit_text(text=text, reply_markup=menu())


@router.message(Branches_req.question1)
async def set_q1(message: Message, state: FSMContext):
    user_id = message.from_user.id
    answer = message.text
    await requests.new_request(user_id)

    text1 = f'<b>Заявка в филиал <code>{user_id}</code> 🙋‍♂️\n\n Ссылка - {answer}</b>'
    await bot.send_message(chat_id=CHANNEL_ID, text=text1, reply_markup=admin_conf_branches(user_id))

    text2 = f'<b>Заявка отправлена!</b>'
    await message.answer(text=text2, reply_markup=menu())
    # try:
    #     await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    # except:
    #     pass