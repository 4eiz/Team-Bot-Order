from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.client import Menu_callback, menu
from data.users import update_wallet

class Wallet(StatesGroup):
    new_wallet = State()

router = Router()


@router.callback_query(Menu_callback.filter(F.menu == 'wallet'))
async def new_wallet(call: CallbackQuery, callback_data: Menu_callback, state: FSMContext):
    await state.set_state(Wallet.new_wallet)
    await call.message.edit_text('<b>Введите адрес кошелька:</b>', reply_markup=menu())



@router.message(Wallet.new_wallet)
async def result(message: Message, state: FSMContext):

    user_id = message.from_user.id
    new_adress = message.text
    await update_wallet(user_id=user_id, new_wallet_value=new_adress)

    
    await message.answer('<b>Кошёлек успешно изменён!</b>', reply_markup=menu())

    await state.clear()