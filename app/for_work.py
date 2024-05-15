from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from keyboards.client import Menu_callback, materials


router = Router()



@router.callback_query(Menu_callback.filter(F.menu == 'for_work'))
async def start_form(call: CallbackQuery, callback_data: Menu_callback):
    text = f'''<b>
👨‍💻Материалы для работы👨‍💻
—————————————————————
🙋‍♂️Запросите индивидуальную ссылку 
с помощью которой можно будет отследить вашу статистику 
( Отправьте запрос по кнопке ниже )

📸Фото и видео модели для работы
└ Фото и видео для Instagram
└ Фото и видео для TikTok
( Перейдите в канал по кнопке ниже )
</b>'''
    await call.message.edit_text(text=text, reply_markup=materials(), disable_web_page_preview=True)
    