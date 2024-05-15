from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.client import Menu_callback, profil_True, profil_False
from data.users import get_user

router = Router()



@router.callback_query(Menu_callback.filter(F.menu == 'profil'))
async def start_form(call: CallbackQuery, callback_data: Menu_callback):
    user_id = call.from_user.id
    user_data = await get_user(user_id)
    # print(user_data)
    wallet = user_data[1]
    if wallet != None:
        text = f'''<b>
💼 Личный кабинет 💼
————————————————————
💳Кошелек - привязан
<code>{wallet}</code>
————————————————————

📎Личные реферальные ссылки📎
————————————————————
🏷️Trial link - НАЖМИ
🖥️Trial monitoring - НАЖМИ

🫰Paid link  - НАЖМИ
🖥️Paid monitoring - НАЖМИ

🤔Реферальные ссылки инфо - ТУТ
————————————————————
</b>'''
        kb = profil_True()


    else:
        text = f'''<b>
💼 Личный кабинет 💼
————————————————————
💳Кошелек - не привязан
————————————————————

📎Личные реферальные ссылки📎
————————————————————
🏷️Trial link - НАЖМИ
🖥️Trial monitoring - НАЖМИ

🫰Paid link  - НАЖМИ
🖥️Paid monitoring - НАЖМИ

🤔Реферальные ссылки инфо - ТУТ
————————————————————
</b>'''
        kb = profil_False()

        
    await call.message.edit_text(text=text, reply_markup=kb)