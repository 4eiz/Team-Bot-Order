import aiofiles
import os

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.client import Answer_callback, accept, decline, Menu_callback, menu
from data.urls import delete_req
from config import bot

router = Router()





@router.callback_query(Answer_callback.filter(F.answer == 'accept_urls'))
async def accept_req(call: CallbackQuery, callback_data: Answer_callback, state: FSMContext):
    user_id = callback_data.user_id
    await delete_req(user_id)

    trial_link, trial_monitoring, paid_link, paid_monitoring = await read_links()
    print('trial_link: ', trial_link)
    print('trial_monitoring: ', trial_monitoring)
    print('paid_link: ', paid_link)
    print('paid_monitoring: ', paid_monitoring)
    text2 = f'<b>✅ Ваша заявка на получение ссылок была одобрена. Загляните в профиль, чтобы их увидеть.</b>'

    await bot.send_message(chat_id=user_id, text=text2, reply_markup=menu())
    await call.message.edit_reply_markup(reply_markup=accept())
    await state.clear()



@router.callback_query(Answer_callback.filter(F.answer == 'decline_urls'))
async def decline_req(call: CallbackQuery, callback_data: Answer_callback):
    user_id = callback_data.user_id
    text = f'<b>❌ Заявка не получение ссылок была отклонена.</b>'
    await delete_req(user_id)
    await call.message.edit_reply_markup(reply_markup=decline())
    await bot.send_message(chat_id=user_id, text=text)



async def read_links():
    current_directory = os.getcwd()
    path = f'{current_directory}/data/db/urls_files'
    trial_path = os.path.join(path, 'urls_trial.txt')
    paid_path = os.path.join(path, 'urls_paid.txt')

    # Общая логика для чтения и удаления первой строки из файла
    async def process_file(file_path):
        # Чтение всего файла в память
        async with aiofiles.open(file_path, 'r') as file:
            lines = await file.readlines()
        
        if not lines:
            return None  # В файле нет содержимого

        # Извлечение и удаление первой строки
        first_line = lines.pop(0).strip()

        # Перезапись файла без первой строки
        async with aiofiles.open(file_path, 'w') as file:
            await file.writelines(lines)

        return first_line

    # Чтение и обработка файлов
    trial_content = await process_file(trial_path)
    paid_content = await process_file(paid_path)

    if trial_content and paid_content:
        trial_link, trial_monitoring = trial_content.split(' | ')
        paid_link, paid_monitoring = paid_content.split(' | ')
        return trial_link, trial_monitoring, paid_link, paid_monitoring
    else:
        return None, None, None, None