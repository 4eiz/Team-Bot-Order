from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.client import Menu_callback, familiarization
from config import link1, link2, link3

router = Router()



@router.callback_query(Menu_callback.filter(F.menu == 'familiarization'))
async def start_form(call: CallbackQuery, callback_data: Menu_callback):
    text = f'''<b>
📰Ознакомление с направлением📰
—————————————————————
📯Наша команда занимается переливом траффика с разных платформ на OnlyFans
—————————————————————

🚀Все что вам нужно для работы🚀
—————————————————————
└ Ознакомление с инструкциями
└ IPhone / IPad ( желательно )
└ Старание и упорность

🤑Касаемо заработка и перспектив🤑
—————————————————————
💎Доведем до профита от 40$ в день 
└ Подробная информация в инструкции
</b>'''
    await call.message.edit_text(text=text, reply_markup=familiarization(), disable_web_page_preview=True)