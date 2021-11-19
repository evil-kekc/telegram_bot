from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from keyboards import kb_client, back_button, album_all_kb
from create_bot import dp, bot


admin_id = chat_id_1, chat_id_2



class FSMAdmin(StatesGroup):
    cm_load = State()
    photo = State()
    num = State()
    description = State()
    price = State()



"""Разрешение на загрузку новых данных через админку. """
async def cm_start(message: types.Message):
    await FSMAdmin.next()
    await message.answer('Выберите, что хотите сделать\n\nДля отмены в любой момент нажмите "Отмена" или /cancel',
                         reply_markup=admin_kb.button_exit_admin)


async def cancel(message: types.Message, state=FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('Ввод отменен', reply_markup=kb_client)


async def cm_load(message: types.Message, state: FSMContext):
    await FSMAdmin.photo.set()
    await message.answer('Загрузите фото', reply_markup=admin_kb.button_cancel_admin)


async def get_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:  # Доступ машине состояний к словарю
        data['photo'] = message.photo[0].file_id  # Сохранение полученного сообщения в словарь
    await FSMAdmin.next()  # Перевод бота в следующее состояние
    await message.reply('Введите номер букета')


async def get_num(message: types.Message, state: FSMContext):
    async with state.proxy() as data:  # Сохранение полученного сообщения в словарь
        data['num'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите описание')


async def get_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:  # Сохранение полученного сообщения в словарь
        data['description'] = message.text
    await FSMAdmin.next()
    await message.reply('Введите цену')


async def get_price(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:  # Сохранение полученного сообщения в словарь
            data['price'] = float(message.text)

        await sqlite_db.sql_add_admin_command(state)  # Передаем наш словать машины состояний в БД
        await message.answer('Данные успешно сохранены\n\n'
                             'Для добавления нажмите "Загрузить", для выхода нажмите "Выход"',
                             reply_markup=admin_kb.button_exit_admin)

        await state.finish()  # Завершаем машину состояний
    except:
        await message.answer('Произошла ошибка сохранения, проверьте правильность ввода данных',
                             reply_markup=kb_client)
        await state.finish()
        

async def client_inf(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await sqlite_db.sql_read_zakaz(message)
    await message.answer('Выберите, что хотите сделать\n\nДля отмены в любой момент нажмите "Отмена" или /cancel',
                         reply_markup=admin_kb.button_exit_admin)
    
        
async def back_button_reply(message: types.Message):

    await bot.send_message(chat_id, text='Нажмите "назад" для возврата к оформлению заказа',
                           reply_markup=back_button)
    await bot.send_message(chat_id, text='Нажмите "назад" для возврата к оформлению заказа',
                           reply_markup=back_button)
    await bot.send_message(chat_id, text='Нажмите "назад" для возврата к оформлению заказа',
                           reply_markup=back_button)
    await bot.send_message(chat_id, text='Также можете посмотреть наши альбомы по ценовым категориям',
                           reply_markup=album_all_kb)
    await bot.send_message(chat_id, text='Нажмите "назад" для возврата к оформлению заказа',
                           reply_markup=back_button)
    await bot.send_message(message.from_user.id,
                           f'Сообщения в чаты отправлены',
                           reply_markup=kb_client)


def register_handlers_admin(dp: Dispatcher):  # Функция для регистрации хэндлерова
    dp.register_message_handler(cm_start, chat_id=admin_id, commands='admin', state=None)

    dp.register_message_handler(cancel, state="*", commands=['отмена', 'cancel'])
    dp.register_message_handler(cancel, Text(equals='отмена', ignore_case=True), state="*")


    dp.register_message_handler(cm_load, Text(equals='Загрузить'), state=FSMAdmin.cm_load)
    dp.register_message_handler(cm_load, commands='Загрузить', state=FSMAdmin.cm_load)

    dp.register_message_handler(get_photo, content_types=['photo'], state=FSMAdmin.photo)

    dp.register_message_handler(get_num, state=FSMAdmin.num)

    dp.register_message_handler(get_description, state=FSMAdmin.description)

    dp.register_message_handler(get_price, state=FSMAdmin.price)

    dp.register_message_handler(back_button_reply, commands=['button'])
    
    dp.register_message_handler(client_inf, Text(equals=['Информация о заказах'], ignore_case=True), state='*')
