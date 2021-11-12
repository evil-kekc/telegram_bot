from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from keyboards.client_kb import url_kb_2, album_kb, album_inst_kb, only_button_cancel, otpr_kb, contact_cancel_button
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import time
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup



class FSMClient(StatesGroup):
    get_ques = State()
    get_otz = State()
    question = State()
    otz = State()
    send_question_otz = State()


storage = MemoryStorage()

async def anti_flood(*args, **kwargs):
    m = args[0]
    await m.answer('Слишком много сообщений, попробуй позже')
    time.sleep(20)




@dp.throttled(anti_flood, rate=3)

async def start_mess(message: types.Message):
    user_name = message.from_user.first_name
    try:
        await bot.send_message(message.from_user.id,
                               f'Привет {user_name}, я маленький бот цветочного магазина vsemcveti.by',
                               reply_markup=kb_client)

    except:
        await message.reply('Общение с ботом происходит через личные сообщения\nНапишите ему: @vsemcvety_bot')
        await message.delete()  # Удаляем сообщение


@dp.throttled(anti_flood, rate=3)
async def work_time(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Пн-Сб: с 10:00 до 20:00\nВс: с 10:00 до 19:00\n\n'
                                                     'В праздничные дни работаем до последнего клиента',
                               reply_markup=kb_client)
    except:
        await message.reply('Общение с ботом происходит через личные сообщения\nНапишите ему: @vsemcvety_bot')
        await message.delete()  # Удаляем сообщение


@dp.throttled(anti_flood, rate=3)
async def place(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Мы находимся по адресу: ул. Барыкина 86', reply_markup=kb_client)
        await bot.send_location(message.from_user.id, latitude=52.418068, longitude=30.978902)
        await bot.send_message(message.from_user.id, 'Если после просмотра карты пропали кнопки и не знаете, как их вернуть:'
                                                     '\n<b>Нажмите</b>  ➡️ /start', parse_mode=types.ParseMode.HTML)
    except:
        await message.reply('Общение с ботом происходит через личные сообщения\nНапишите ему: @vsemcvety_bot')
        await message.delete()  # Удаляем сообщение


async def del_button(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, '<b>Нажмите пожалуйста</b>  ➡️ /start',
                               parse_mode=types.ParseMode.HTML, reply_markup=ReplyKeyboardRemove())
    except:
        await message.reply('Общение с ботом происходит через личные сообщения\nНапишите ему: @vsemcvety_bot')
        await message.delete()  # Удаляем сообщение


@dp.throttled(anti_flood, rate=3)
async def album_command(message: types.Message):
    # await sqlite_db.sql_read_admin(message)
    await message.answer('Выберите один из наших альбомов', reply_markup=album_inst_kb)
    await bot.send_message(message.from_user.id, 'Также можете заглянуть в наш instagram :)', reply_markup=album_kb)

async def zakaz_1(message: types.Message):
    await message.answer('Для оформления заказа напишите: /order')

async def contact_inf(message: types.Message):
    await message.answer('<b>Наши контакты:</b>\n\n☎ +375293377277', parse_mode=types.ParseMode.HTML,
                         reply_markup=url_kb_2)



async def get_num_ques(message:types.Message):
    await message.answer('Введите ваш номер телефона', reply_markup=contact_cancel_button)
    await FSMClient.get_ques.set()

async def get_num_otz(message:types.Message):
    await message.answer('Введите ваш номер телефона', reply_markup=contact_cancel_button)
    await FSMClient.get_otz.set()


async def get_ques(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await message.answer('Ввод отменен', reply_markup=kb_client)
        await state.finish()
    else:
        number = message.text
        if number == None:
            contact = message.contact
            number = (f'\n  Имя:{contact.full_name}\n  Телефон: {contact.phone_number}\n  ID: {contact.user_id}')
        await state.update_data(number=number)
        await message.answer('Введите ваш вопрос', reply_markup=only_button_cancel)
        await FSMClient.question.set()



async def get_otz(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await message.answer('Ввод отменен', reply_markup=kb_client)
        await state.finish()
    else:
        number_1 = message.text
        if number_1 == None:
            contact_1 = message.contact
            number_1 = (f'\n  Имя:{contact_1.full_name}\n  Телефон: {contact_1.phone_number}\n  ID: {contact_1.user_id}')

        await state.update_data(number_1=number_1)
        await message.answer('Введите ваш отзыв', reply_markup=only_button_cancel)
        await FSMClient.otz.set()

async def question(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await message.answer('Ввод отменен', reply_markup=kb_client)
        await state.finish()
    else:
        question = message.text
        await state.update_data(question=question)
        await message.answer('Для отправки вопроса нажмите "отправить"', reply_markup=otpr_kb)
        await FSMClient.send_question_otz.set()

async def otz(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await message.answer('Ввод отменен', reply_markup=kb_client)
        await state.finish()
    else:
        otz = message.text
        await state.update_data(otz=otz)
        await message.answer('Для отправки отзыва нажмите "отправить"', reply_markup=otpr_kb)
        await FSMClient.send_question_otz.set()


async def send_question_otz(message: types.Message, state: FSMContext):
    if message.text == 'Отмена':
        await message.answer('Ввод отменен', reply_markup=kb_client)
        await state.finish()
    else:
        data = await state.get_data()
        question = data.get('question')
        data = await state.get_data()
        otz = data.get('otz')
        data = await state.get_data()
        number = data.get('number')
        data = await state.get_data()
        number_1 = data.get('number_1')



        user_name = message.from_user.first_name
        user_surname = message.from_user.last_name

        await message.answer('Спасибо за информацию, с вами вскоре свяжутся', reply_markup=kb_client)
        if otz == None:
            if user_surname == None:
                await bot.send_message(-1001558893104, f'<b>Поступил новый вопрос!</b>\n\n'
                                                       f'<b>Пользователь:</b> {user_name}\n'
                                                       f'<b>Контакт:</b> {number}\n'
                                                       f'<b>Вопрос:</b> {question}\n',
                                       parse_mode=types.ParseMode.HTML)
            else:
                await bot.send_message(-1001558893104, f'<b>Поступил новый вопрос!</b>\n\n'
                                                       f'<b>Пользователь:</b> {user_name} {user_surname}\n'
                                                       f'<b>Контакт:</b> {number}\n'
                                                       f'<b>Вопрос:</b> {question}\n',
                                       parse_mode=types.ParseMode.HTML)

        elif question == None:
            if user_surname == None:
                await bot.send_message(-1001558893104, f'<b>Поступил новый отзыв!</b>\n\n'
                                                       f'<b>Пользователь:</b> {user_name}\n'
                                                       f'<b>Контакт:</b> {number_1}\n'
                                                       f'<b>Вопрос:</b> {otz}\n',
                                       parse_mode=types.ParseMode.HTML)
            else:
                await bot.send_message(-1001558893104, f'<b>Поступил новый отзыв!</b>\n\n'
                                                       f'<b>Пользователь:</b> {user_name} {user_surname}\n'
                                                       f'<b>Контакт:</b> {number_1}\n'
                                                       f'<b>Вопрос:</b> {otz}\n',
                                       parse_mode=types.ParseMode.HTML)

        await state.finish()

def register_handlers_client(dp: Dispatcher):  # Функция для регистрации хэндлерова
    dp.register_message_handler(start_mess, Text(equals='Выход'))
    dp.register_message_handler(start_mess, Text(equals='Отмена'))

    dp.register_message_handler(start_mess, commands=['start', 'help'])

    dp.register_message_handler(work_time, Text(equals='🕗 Режим работы', ignore_case=True))
    dp.register_message_handler(work_time, commands=['Режим_работы'])

    dp.register_message_handler(place, Text(equals='📍Адрес магазина', ignore_case=True))
    dp.register_message_handler(place, commands=['Адрес_магазина'])

    dp.register_message_handler(del_button, Text(equals='❌ Убрать кнопки', ignore_case=True))
    dp.register_message_handler(del_button, commands=['Убрать_кнопки'])

    dp.register_message_handler(album_command, Text(equals='📁 Альбом', ignore_case=True))
    dp.register_message_handler(album_command, commands='Альбом')


    dp.register_message_handler(contact_inf, Text(equals='☎️ Связь с нами'))
    # dp.register_message_handler(zakaz_1, lambda message: 'Заказать' or 'заказать' in message.text)

    dp.register_message_handler(zakaz_1, Text(equals=['заказать', 'заказ'], ignore_case=True))

    dp.register_message_handler(get_num_ques, Text(equals='❓Задать вопрос'), state=None)
    dp.register_message_handler(get_num_otz, Text(equals='⚠️Оставить отзыв'), state=None)

    dp.register_message_handler(get_ques, content_types=types.ContentType.CONTACT, state=FSMClient.get_ques)
    dp.register_message_handler(get_ques, state=FSMClient.get_ques)

    dp.register_message_handler(get_otz, content_types=types.ContentType.CONTACT, state=FSMClient.get_ques)
    dp.register_message_handler(get_otz, state=FSMClient.get_otz)

    dp.register_message_handler(otz, state=FSMClient.otz)

    dp.register_message_handler(question, state=FSMClient.question)

    dp.register_message_handler(send_question_otz, content_types=types.ContentType.CONTACT, state=FSMClient.send_question_otz)
    dp.register_message_handler(send_question_otz, state=FSMClient.send_question_otz)


