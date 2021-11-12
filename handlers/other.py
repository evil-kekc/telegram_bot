from aiogram import types, Dispatcher
from create_bot import bot, dp
import json, string
from aiogram.dispatcher.handler import SkipHandler


async def mat_fill(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')} \
            .intersection(set(json.load(open('cenz.json')))) != set():  # Генератор множеств, в котором получаем сообщение, добавляем разделитель, прохоимся по нему циклом и убираем все маскирующие символы
        await message.reply('Маты запрещены')
        await message.delete()
    else:
        raise SkipHandler



async def start_mess(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, '<b>Нажмите пожалуйста</b>  ➡️ /start', parse_mode=types.ParseMode.HTML)
    except:
        await message.reply('Общение с ботом происходит через личные сообщения\nНапишите ему: @vsemcvety_bot')
        await message.delete()  # Удаляем сообщение

def register_handlers_other(dp: Dispatcher):  # Функция для регистрации хэндлерова
    dp.register_message_handler(mat_fill)
    dp.register_message_handler(start_mess)

