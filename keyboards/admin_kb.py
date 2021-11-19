from aiogram.types import KeyboardButton, ReplyKeyboardMarkup



"""Кнопки клавиатуры админа"""

button_load = KeyboardButton('Загрузить')
button_cancel = KeyboardButton('Отмена')
button_exit = KeyboardButton('Выход')
button_client_inf = KeyboardButton('Информация о заказах')





button_case_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load).add(button_cancel)

button_cancel_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_cancel)

button_exit_admin = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_load)\
    .add(button_client_inf).add(button_exit)

button_choise_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add().add(button_exit)
