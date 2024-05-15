from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.client import Menu_callback, menu
from data.admin import get_offers


router = Router()



@router.callback_query(Menu_callback.filter(F.menu == 'offers'))
async def start_form(call: CallbackQuery, callback_data: Menu_callback):
    text = await get_offers()
    text = f'<b>{text}</b>'
    await call.message.edit_text(text=text, reply_markup=menu(), disable_web_page_preview=True)