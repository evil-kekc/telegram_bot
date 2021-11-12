"""Клавиатура клиента"""

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



"""****************************Обычные кнопки****************************"""


button_1 = KeyboardButton('🕗 Режим работы')
button_2 = KeyboardButton('📍Адрес магазина')
button_3 = KeyboardButton('📁 Альбом')
button_4 = KeyboardButton('☎️ Связь с нами')
button_5 = KeyboardButton('❌ Убрать кнопки')
button_6 = KeyboardButton('Посмотреть альбом')
button_7 = KeyboardButton('✅ ОФОРМИТЬ ЗАКАЗ ✅')  # Отправлям свое местоположение
button_8 = KeyboardButton('Поделиться номером', request_contact=True)  # Отправляем свой контакт
# button_9 = KeyboardButton('Мое местоположение', request_location=True)  # Отправлям свое местоположение




button_telephone = KeyboardButton('Телефон')
button_viber = KeyboardButton('Viber')
button_telegram = KeyboardButton('Telegram')
button_whatsapp = KeyboardButton('Whatsapp')
button_rand = KeyboardButton('Без разницы')
button_cancel_client = KeyboardButton('Отмена')
question_button = KeyboardButton('❓Задать вопрос')
otz_button = KeyboardButton('⚠️Оставить отзыв')
otpr_button = KeyboardButton('Отправить')
ind_button = KeyboardButton('Хочу индивидуальный букет')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True).add(button_1).row(button_2, button_3).add(button_7)\
    .row(question_button, otz_button).add(button_4).add(button_5)

otpr_kb = ReplyKeyboardMarkup(resize_keyboard=True).add(otpr_button).add(button_cancel_client)

button_cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_6)\
    .add(button_cancel_client)
button_album = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_3).add(button_cancel_client)

button_choise_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_telephone)\
    .row(button_viber, button_telegram).add(button_whatsapp).add(button_rand).add(button_cancel_client)

only_button_cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_cancel_client)

individul_cancel_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(ind_button)\
    .add(button_cancel_client)

contact_cancel_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button_8)\
    .add(button_cancel_client)

question_button = KeyboardButton(text='Задать вопрос', callback_data='question')

otz_button = KeyboardButton(text='Оставить отзыв', callback_data='otz')

question_otz_button = ReplyKeyboardMarkup(resize_keyboard=True).add(question_button).add(otz_button)



"""*********************************Inline кноки*********************************"""



inst_button = InlineKeyboardButton(text='Наш инстаграм', url='https://instagram.com/vsemcveti.by?utm_medium=copy_link')
telegram_button = InlineKeyboardButton(text='Наш телеграм', url='https://t.me/flowersgomel')
album_button_inline = InlineKeyboardButton(text='Наш общий альбом', url='https://t.me/flowersgomel')

url_kb_1 = InlineKeyboardMarkup(resize_keyboard=True).add(inst_button)

url_kb_2 = InlineKeyboardMarkup(resize_keyboard=True).add(inst_button).add(telegram_button)

album_kb = InlineKeyboardMarkup(resize_keyboard=True).add(inst_button)

album = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton(text='Альбом', callback_data='album'))

price_kb = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton(text='Альбом с букетами до 50 BYN',
                                                                               url='t.me/vsemcveti_album_0_50'))\
    .add(InlineKeyboardButton(text='Альбом с букетами от 50 до 100 BYN', url='t.me/vsemcveti_album_50_100'))\
    .add(InlineKeyboardButton(text='Альбом с букетами от 100 BYN', url='t.me/vsemcveti_album_100'))

album_inst_kb = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton(text='Альбом с букетами до 50 BYN',
                                                                                    url='t.me/vsemcveti_album_0_50'))\
    .add(InlineKeyboardButton(text='Альбом с букетами от 50 до 100 BYN', url='t.me/vsemcveti_album_50_100'))\
    .add(InlineKeyboardButton(text='Альбом с букетами от 100 BYN', url='t.me/vsemcveti_album_100'))\
    .add(InlineKeyboardButton(text='Наш общий альбом', url='https://t.me/flowersgomel'))

yes_no_kb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Да', callback_data='yes')).\
    add(InlineKeyboardButton(text='Нет', callback_data='no'))

back_button = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Назад', url='t.me/vsemcvety_bot'))

album_all_kb = InlineKeyboardMarkup(resize_keyboard=True).add(InlineKeyboardButton(text='Альбом с букетами до 50 BYN',
                                                                                   url='t.me/vsemcveti_album_0_50'))\
    .add(InlineKeyboardButton(text='Альбом с букетами от 50 до 100 BYN', url='t.me/vsemcveti_album_50_100'))\
    .add(InlineKeyboardButton(text='Альбом с букетами от 100 BYN', url='t.me/vsemcveti_album_100'))


