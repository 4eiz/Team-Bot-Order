from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.client import Menu_callback, menu


router = Router()



@router.callback_query(Menu_callback.filter(F.menu == 'payments'))
async def start_form(call: CallbackQuery, callback_data: Menu_callback):
    text = f'''<b>
💎Отправьте запрос на выплату💎
————————————————————
⚖️Выплата происходит при условии:
└ От 10$ на реферальной ссылке
└ Кошелек привязан к боту

————————————————————
📌Привяжи кошелек для выплат📌
————————————————————
</b>'''
    await call.message.edit_text(text=text, reply_markup=menu())
    