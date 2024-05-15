from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.client import Menu_callback, menu


router = Router()



@router.callback_query(Menu_callback.filter(F.menu == 'support'))
async def start_form(call: CallbackQuery, callback_data: Menu_callback):
    text = '''<b>
⚙️Поддержка⚙️
———————————————
TC - @boxer_curator
Curator - @magcvv
Support - @laplas19
———————————————
</b>'''
    await call.message.edit_text(text=text, reply_markup=menu(), disable_web_page_preview=True)