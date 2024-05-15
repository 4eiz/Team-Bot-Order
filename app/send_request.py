from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from keyboards.client import Menu_callback, cancel, confirm, admin_conf, Answer_callback
from data import requests
from config import bot, CHANNEL_ID

router = Router()

class Form(StatesGroup):
    question1 = State()
    question2 = State()
    question3 = State()
    conf = State()

remove = ReplyKeyboardRemove()


#--------------------------------------

@router.message(F.text.lower() == 'отмена')
@router.message(Menu_callback.filter(F.menu == 'cancel'), Form.conf)
async def cancel1(message: Message, state: FSMContext):
    await message.answer('<b>Отменено</b>', reply_markup=remove)
    await state.clear()

# @router.message(Menu_callback.filter(F.menu == 'cancel'), Form.conf)
# async def cancel2(call: CallbackQuery, callback_data: Menu_callback, state: FSMContext):
#     await call.message.answer('<b>Отменено</b>', reply_markup=remove)
#     await state.clear()

#--------------------------------------


@router.callback_query(Menu_callback.filter(F.menu == 'request'))
async def start_form(call: CallbackQuery, callback_data: Menu_callback, state: FSMContext):
    try:
        await state.clear()
    except:
        pass
    user_id = call.from_user.id
    user = await requests.check_req_in_database(user_id)
    if user == True:
        await call.message.answer(text='<b>Вы уже отправили заявку</b>')
    else:
        await state.set_state(Form.question1)
        await call.message.answer('<b>Имеете ли вы опыт в УБД траффике?</b>', reply_markup=cancel())


@router.message(Form.question1)
async def set_q1(message: Message, state: FSMContext):
    answer1 = message.text

    await message.answer('<b>Сколько времени готовы уделять работе?</b>', reply_markup=cancel())
    await state.update_data(answer1 = answer1)
    await state.set_state(Form.question2)


@router.message(Form.question2)
async def set_q2(message: Message, state: FSMContext):
    answer2 = message.text

    await message.answer('<b>С какого устройства вы будете работать?</b>', reply_markup=cancel())
    await state.update_data(answer2 = answer2)
    await state.set_state(Form.question3)


@router.message(Form.question3)
async def set_q3(message: Message, state: FSMContext):
    form_data = await state.get_data()
    answer1 = form_data.get('answer1')
    answer2 = form_data.get('answer2')
    answer3 = message.text
    await state.update_data(answer3 = answer3)

    text = f'<b>Ваша анкета:\n\n1. Имелся ли опыт в УБТ траффике?\nВаш ответ - {answer1}\n2. Сколько времени готовы уделять?\nВаш ответ - {answer2}\n3. С какого устройства вы будете работать?\nВаш ответ - {answer3}</b>'

    await message.answer(text=text, reply_markup=confirm())
    await state.set_state(Form.conf)
    

@router.callback_query(Menu_callback.filter(F.menu == 'send_request'), Form.conf)
async def confirm_request(call: CallbackQuery, callback_data: Menu_callback, state: FSMContext):
    form_data = await state.get_data()
    answer1 = form_data.get('answer1')
    answer2 = form_data.get('answer2')
    answer3 = form_data.get('answer3')

    user_id = call.from_user.id
    print(user_id)
    await requests.new_request(user_id)

    text1 = f'<b>Анкета юзера <code>{user_id}</code>:\n\n1. Имелся ли опыт в УБТ траффике?\nОтвет - {answer1}\n2. Сколько времени готовы уделять?\nОтвет - {answer2}\n3. С какого устройства вы будете работать?\nОтвет - {answer3}</b>'
    await bot.send_message(chat_id=CHANNEL_ID, text=text1, reply_markup=admin_conf(user_id))

    text2 = f'<b>Анкета отправлена!</b>'
    await call.message.answer(text=text2, reply_markup=remove)
    try:
        await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    except:
        pass

    await state.clear()