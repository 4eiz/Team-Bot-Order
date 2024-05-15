from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.client import Menu_callback, offers_cancel, worker_menu_admin
from data import users
from config import bot

class Admin(StatesGroup):
    new_message = State()

router = Router()


@router.callback_query(Menu_callback.filter(F.menu == 'newsletter'))
async def new_mes(call: CallbackQuery, callback_data: Menu_callback, state: FSMContext):
    await state.set_state(Admin.new_message)
    await call.message.edit_text('<b>Введите сообщение рассылки:</b>', reply_markup=offers_cancel())



@router.message(Admin.new_message)
async def result(message: Message, state: FSMContext):
  
    new_mes = message.text
    user_table = await users.get_all_ids_from_db()
    for user in user_table:
        try:
            await bot.send_message(user, new_mes)
        except Exception as e:
            print(e)
    
    await message.answer('<b>Рассылка успешно запущена!</b>')
    await message.answer(f'<b>👋 Здравствуйте, {message.from_user.first_name}!\n\n'
                        'Вы сейчас находитесь в главном меню.</b>', reply_markup=worker_menu_admin())

    await state.clear()