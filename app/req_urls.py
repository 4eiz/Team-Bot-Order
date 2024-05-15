from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.client import Menu_callback, send_req_urls, menu, admin_conf_urls
from config import bot, CHANNEL_ID_URLS
from data.urls import new_request
from data.fillials import get_fillial_info

router = Router()


class Urls_req(StatesGroup):
    question1 = State()




@router.callback_query(Menu_callback.filter(F.menu == 'url_req'))
async def kb_start(call: CallbackQuery, callback_data: Menu_callback):

    text = f'<b>Хотите ли вы отправить заявку на получение ссылок?</b>'


    await call.message.edit_text(text=text, reply_markup=send_req_urls())



@router.callback_query(Menu_callback.filter(F.menu == 'send_req_urls'))
async def send(call: CallbackQuery, callback_data: Menu_callback):
    user_id = call.from_user.id
    await new_request(user_id)

    text1 = f'<b>Заявка на получение ссылок <code>{user_id}</code> 📎</b>'
    await bot.send_message(chat_id=CHANNEL_ID_URLS, text=text1, reply_markup=admin_conf_urls(user_id))

    text2 = f'<b>Заявка отправлена!</b>'
    await call.message.edit_text(text=text2, reply_markup=menu())