from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.client import Menu_callback, menu, instructions


router = Router()



@router.callback_query(Menu_callback.filter(F.menu == 'manuals'))
async def start_form(call: CallbackQuery, callback_data: Menu_callback):
    text = '''<b>
📖Все инструкции для работы 📖
—————————————————————
📍Внимательно ознакомитесь со всеми разделами данной инструкции по кнопке ниже ( вас перенаправит в браузер )
—————————————————————

🤔С чем вы ознакомитесь ниже:
└ Общая информация о команде
└ Терминология и общие понятия
└ Настройка телефона под пролив
└ Настройка и прогрев Instagram
└ Правильный пролив в TikTok
└ Оплата и многое другое…
</b>'''
    await call.message.edit_text(text=text, reply_markup=instructions())