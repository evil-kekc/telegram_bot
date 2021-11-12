from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from create_bot import dp, bot
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import kb_client, client_kb, yes_no_kb, only_button_cancel, price_kb, individul_cancel_button,\
    contact_cancel_button
from aiogram.dispatcher.filters import Text


class FSMZakaz(StatesGroup):
    photo = State()
    type_commun = State()
    yes_no = State()
    get_adr = State()
    get_date = State()
    get_time_dost = State()
    get_contact = State()

    tel_numb = State()


async def cm_start(message: types.Message):
    await message.answer('Введите номер или отправьте фото желаемого букета\n'
                         'Также можете переслать фото из любого из наших альбомов '
                         'или отправиль ссылку на фото из instagram\n\n'
                         'Для отмены нажмите "Отмена"', reply_markup=individul_cancel_button)
    await message.answer('Если еще не выбрали букет, загляните в наш альбом!', reply_markup=price_kb)
    await FSMZakaz.photo.set()


async def get_photo(message: types.Message, state: FSMContext):
    if message.content_type == 'photo':
        async with state.proxy() as data:  # Сохранение полученного сообщения в словарь
            data['photo'] = message.photo[0].file_id

        await message.answer('Выберите предпочтительный тип связи', reply_markup=client_kb.button_choise_client)
    else:
        number = message.text
        await state.update_data(flow_num=number)

        await message.answer('Выберите предпочтительный тип связи', reply_markup=client_kb.button_choise_client)

        await FSMZakaz.type_commun.set()

async def get_num(message: types.Message, state: FSMContext):
    if message.text == 'Посмотреть альбом':
        await state.finish()
        await message.answer('Выберите нужную кнопку', reply_markup=client_kb.button_album)

    else:
        async with state.proxy() as data:  # Сохранение полученного сообщения в словарь
            data['number'] = message.text
        await message.answer('Выберите предпочтительный тип связи', reply_markup=client_kb.button_choise_client)
        await FSMZakaz.type_commun.set()


async def telephone(message: types.Message, state: FSMContext):
    type_communicate = message.text
    await state.update_data(type_cummunicate=type_communicate)
    await message.answer('Нужна доставка?\nПри заказе от 45р доставка бесплатная', reply_markup=yes_no_kb)
    await FSMZakaz.yes_no.set()



async def viber(message: types.Message, state: FSMContext):
    type_communicate = message.text
    await state.update_data(type_cummunicate=type_communicate)
    await message.answer('Нужна доставка?\nПри заказе от 45р доставка бесплатная', reply_markup=yes_no_kb)
    await FSMZakaz.yes_no.set()



async def telegram(message: types.Message, state: FSMContext):
    type_communicate = message.text
    await state.update_data(type_cummunicate=type_communicate)
    await message.answer('Нужна доставка?\nПри заказе от 45р доставка бесплатная', reply_markup=yes_no_kb)
    await FSMZakaz.yes_no.set()


async def whatsapp(message: types.Message, state: FSMContext):
    type_communicate = message.text
    await state.update_data(type_communicate=type_communicate)
    await message.answer('Нужна доставка?\nПри заказе от 45р доставка бесплатная', reply_markup=yes_no_kb)
    await FSMZakaz.yes_no.set()


async def rand(message: types.Message, state: FSMContext):
    type_communicate = message.text
    await state.update_data(type_cummunicate=type_communicate)
    await message.answer('Нужна доставка?\nПри заказе от 50р доставка бесплатная', reply_markup=yes_no_kb)
    await FSMZakaz.yes_no.set()


async def dost_yes(callback: types.CallbackQuery, state: FSMContext):
    dost_yes = 'Да'
    await state.update_data(dost_yes=dost_yes)
    await callback.message.answer('Введите адрес доставки', reply_markup=only_button_cancel)
    await callback.answer()
    await FSMZakaz.get_adr.set()


async def get_adr(message: types.Message, state: FSMContext):
    adr_dost = message.text
    await state.update_data(adr_dost=adr_dost)
    await message.answer('Введите дату доставки', reply_markup=only_button_cancel)
    await FSMZakaz.get_date.set()


async def get_date_dost(message: types.Message, state: FSMContext):
    date_dost = message.text
    await state.update_data(date_dost=date_dost)
    await message.answer('Введите время доставки', reply_markup=only_button_cancel)
    await FSMZakaz.get_time_dost.set()


async def get_time_dost(message: types.Message, state: FSMContext):
    time_dost = message.text
    await state.update_data(time_dost=time_dost)
    await message.answer('Введите телефон получателя', reply_markup=only_button_cancel)
    await FSMZakaz.get_contact.set()



async def get_cont_num(message: types.Message, state: FSMContext):
    contact = message.text
    await state.update_data(contact=contact)
    await message.answer('Введите ваш номер телефона или нажмите "поделиться номером"', reply_markup=contact_cancel_button)
    await FSMZakaz.tel_numb.set()


async def dost_no(callback: types.CallbackQuery, state: FSMContext):
    dost_no = 'Нет'
    await state.update_data(dost_no=dost_no)
    await callback.message.answer('Введите ваш номер телефона или нажмите "поделиться номером"', reply_markup=contact_cancel_button)
    await callback.answer()
    await FSMZakaz.tel_numb.set()




async def get_tel(message: types.Message, state: FSMContext):
    data = await state.get_data()
    number = data.get('flow_num')
    data = await state.get_data()
    type_communicate = data.get('type_cummunicate')
    data = await state.get_data()
    dost_yes = data.get('dost_yes')
    data = await state.get_data()
    adr_dost = data.get('adr_dost')
    data = await state.get_data()
    date_dost = data.get('date_dost')
    data = await state.get_data()
    time_dost = data.get('time_dost')
    data = await state.get_data()
    contact = data.get('contact')
    data = await state.get_data()
    dost_no = data.get('dost_no')
    data = await state.get_data()
    photo = data.get('photo')


    user_name = message.from_user.first_name
    user_surname = message.from_user.last_name

    telephone = message.text
    if telephone == None:
        contact_1 = message.contact
        telephone = (f'\n  Имя:{contact_1.full_name}\n  Телефон: {contact_1.phone_number}\n  ID: {contact_1.user_id}')

    # await sqlite_db.sql_add_zakaz_command(state)

    await message.answer('Спасибо за заказ, с вами вскоре свяжутся', reply_markup=kb_client)
    if dost_yes == None:
        if user_surname == None:
            if photo == None:
                await bot.send_message(-1001558893104, f'<b>Поступил новый заказ!</b>\n\n\n'
                                                       f'<b>Заказчик:</b> {user_name}\n\n'
                                                       f'<b>Номер букета:</b> {number}\n\n'
                                                       f'<b>Контакт заказчика:</b> {telephone}\n\n'
                                                       f'<b>Нужна ли доставка:</b> {dost_no}\n\n'
                                                       f'<b>Тип связи:</b> {type_communicate}',
                                       parse_mode=types.ParseMode.HTML)
            else:
                await bot.send_photo(-1001558893104, photo, f'<b>Поступил новый заказ!</b>\n\n\n'
                                                            f'<b>Заказчик:</b> {user_name}\n\n'
                                                            f'<b>Номер телефона:</b> {telephone}\n\n'
                                                            f'<b>Нужна ли доставка:</b> {dost_no}\n\n'
                                                            f'<b>Тип связи:</b> {type_communicate}',
                                     parse_mode=types.ParseMode.HTML)
        else:
            if photo == None:
                await bot.send_message(-1001558893104, f'<b>Поступил новый заказ!</b>\n\n\n'
                                                       f'<b>Заказчик:</b> {user_name} {user_surname}\n\n'
                                                       f'<b>Номер букета:</b> {number}\n\n'
                                                       f'<b>Контакт заказчика:</b> {telephone}\n\n'
                                                       f'<b>Нужна ли доставка:</b> {dost_no}\n\n'
                                                       f'<b>Тип связи:</b> {type_communicate}',
                                       parse_mode=types.ParseMode.HTML)
            else:
                await bot.send_photo(-1001558893104, photo, f'<b>Поступил новый заказ!</b>\n\n\n'
                                                            f'<b>Заказчик:</b> {user_name} {user_surname}\n\n'
                                                            f'<b>Контакт заказчика:</b> {telephone}\n\n'
                                                            f'<b>Нужна ли доставка:</b> {dost_no}\n\n'
                                                            f'<b>Тип связи:</b> {type_communicate}',
                                     parse_mode=types.ParseMode.HTML)

    elif dost_no == None:
        if user_surname == None:
            if photo == None:
                await bot.send_message(-1001558893104,
                                       f'<b>Поступил новый заказ!</b>\n\n\n'
                                       f'<b>Заказчик:</b> {user_name}\n\n'
                                       f'<b>Номер букета:</b> {number}\n\n'
                                       f'<b>Контакт заказчика:</b> {telephone}\n\n'
                                       f'<b>Нужна ли доставка?:</b> {dost_yes}\n\n'
                                       f'<b>Адрес доставки:</b> {adr_dost}\n\n'
                                       f'<b>Дата доставки:</b> {date_dost}\n\n'
                                       f'<b>Время доставки:</b> {time_dost}\n\n'
                                       f'<b>Номер телефона получателя:</b> {contact}\n\n'
                                       f'<b>Тип связи:</b> {type_communicate}',
                                       parse_mode=types.ParseMode.HTML)
            else:
                await bot.send_photo(-1001558893104, photo, f'<b>Поступил новый заказ!</b>\n\n\n'
                                                            f'<b>Заказчик:</b> {user_name}\n\n'
                                                            f'<b>Контакт заказчика:</b> {telephone}\n\n'
                                                            f'<b>Нужна ли доставка?:</b> {dost_yes}\n\n'
                                                            f'<b>Адрес доставки:</b> {adr_dost}\n\n'
                                                            f'<b>Дата доставки:</b> {date_dost}\n\n'
                                                            f'<b>Время доставки:</b> {time_dost}\n\n'
                                                            f'<b>Номер телефона получателя:</b> {contact}\n\n'
                                                            f'<b>Тип связи:</b> {type_communicate}',
                                     parse_mode=types.ParseMode.HTML)

        else:
            if photo == None:
                await bot.send_message(-1001558893104,
                                       f'<b>Поступил новый заказ!</b>\n\n\n'
                                       f'<b>Заказчик:</b> {user_name} {user_surname}\n\n'
                                       f'<b>Номер букета:</b> {number}\n\n'
                                       f'<b>Контакт заказчика:</b> {telephone}\n\n'
                                       f'<b>Нужна ли доставка?:</b> {dost_yes}\n\n'
                                       f'<b>Адрес доставки:</b> {adr_dost}\n\n'
                                       f'<b>Дата доставки:</b> {date_dost}\n\n'
                                       f'<b>Время доставки:</b> {time_dost}\n\n'
                                       f'<b>Номер телефона получателя:</b> {contact}\n\n'
                                       f'<b>Тип связи:</b> {type_communicate}',
                                       parse_mode=types.ParseMode.HTML)
            else:
                await bot.send_photo(-1001558893104, photo, f'<b>Поступил новый заказ!</b>\n\n\n'
                                                            f'<b>Заказчик:</b> {user_name} {user_surname}\n\n'
                                                            f'<b>Контакт заказчика:</b> {telephone}\n\n'
                                                            f'<b>Нужна ли доставка?:</b> {dost_yes}\n\n'
                                                            f'<b>Адрес доставки:</b> {adr_dost}\n\n'
                                                            f'<b>Дата доставки:</b> {date_dost}\n\n'
                                                            f'<b>Время доставки:</b> {time_dost}\n\n'
                                                            f'<b>Номер телефона получателя:</b> {contact}\n\n'
                                                            f'<b>Тип связи:</b> {type_communicate}',
                                     parse_mode=types.ParseMode.HTML)




    await state.finish()




def register_handlers_zakaz(dp: Dispatcher):  # Функция для регистрации хэндлерова
    dp.register_message_handler(cm_start, Text(equals='✅ ОФОРМИТЬ ЗАКАЗ ✅'), state=None)
    dp.register_message_handler(cm_start, commands=['Оформить_заказ', 'order'], state=None)

    dp.register_message_handler(get_photo, content_types=['photo', 'text'], state=FSMZakaz.photo)

    dp.register_message_handler(telephone, Text(equals='Телефон'), state=FSMZakaz.type_commun)
    dp.register_message_handler(telephone, state=FSMZakaz.type_commun)

    dp.register_message_handler(viber, Text(equals='Viber'), state=FSMZakaz.type_commun)
    dp.register_message_handler(viber, state=FSMZakaz.type_commun)

    dp.register_message_handler(telegram, Text(equals='Telegram'), state=FSMZakaz.type_commun)
    dp.register_message_handler(telegram, state=FSMZakaz.type_commun)

    dp.register_message_handler(whatsapp, Text(equals='Whatsapp'), state=FSMZakaz.type_commun)
    dp.register_message_handler(whatsapp, state=FSMZakaz.type_commun)

    dp.register_message_handler(rand, Text(equals='Без разницы'), state=FSMZakaz.type_commun)
    dp.register_message_handler(rand, state=FSMZakaz.type_commun)

    dp.register_callback_query_handler(dost_yes, text='yes', state=FSMZakaz.yes_no)

    dp.register_message_handler(get_adr, state=FSMZakaz.get_adr)

    dp.register_message_handler(get_date_dost, state=FSMZakaz.get_date)

    dp.register_message_handler(get_time_dost, state=FSMZakaz.get_time_dost)

    dp.register_message_handler(get_cont_num, state=FSMZakaz.get_contact)

    dp.register_callback_query_handler(dost_no, text='no', state=FSMZakaz.yes_no)

    dp.register_message_handler(get_tel, content_types=types.ContentType.CONTACT, state=FSMZakaz.tel_numb)
    dp.register_message_handler(get_tel, state=FSMZakaz.tel_numb)
