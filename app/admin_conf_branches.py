from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.client import Answer_callback, accept, decline, url_chat, send_request, Menu_callback, admin_panel, offers_cancel, worker_menu_admin
from data.requests import delete_req
from data.fillials import new_fillial
from data.admin import update_offers
from config import bot


router = Router()


class Branches_data(StatesGroup):
    data = State()



@router.callback_query(Answer_callback.filter(F.answer == 'accept_branches'))
async def accept_req(call: CallbackQuery, callback_data: Answer_callback, state: FSMContext):
    user_id = callback_data.user_id
    text = '<b>Введите ссылку на чат</b>'
    await call.message.reply(text=text)
    await state.set_state(Branches_data.data)
    await state.update_data(user_id=user_id)
    await call.message.edit_reply_markup(reply_markup=accept())


@router.message(Branches_data.data)
async def accept_req2(message: Message, state: FSMContext):
    channel_url = message.text
    form_data = await state.get_data()
    user_id = form_data.get('user_id')
    # await message.edit_reply_markup(reply_markup=accept())
    await delete_req(user_id)
    await new_fillial(user_id, channel_url)

    text2 = '''<b>
✅ Вы были приняты в филиал
</b>'''

    await bot.send_message(chat_id=user_id, text=text2, reply_markup=url_chat(channel=channel_url))
    await state.clear()





@router.callback_query(Answer_callback.filter(F.answer == 'decline_branches'))
async def decline_req(call: CallbackQuery, callback_data: Answer_callback):
    user_id = callback_data.user_id
    text = '<b>❌ Вы не были приняты в филиал</b>'
    await delete_req(user_id)
    await call.message.edit_reply_markup(reply_markup=decline())
    await bot.send_message(chat_id=user_id, text=text)