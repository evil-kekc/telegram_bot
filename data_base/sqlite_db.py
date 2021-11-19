import sqlite3 as sq
from create_bot import dp, bot


"""Создаем базу данных и/или подключаеимся к ней"""
def sql_start():
    global base, cur
    base = sq.connect('vsemcveti.db')
    cur = base.cursor()
    if base:
        print('\nData base admin connected!')
    base.execute('CREATE TABLE IF NOT EXISTS album(img TEXT, num TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


def sql_start_1():
   global base, cur
    base = sq.connect('vsemcveti.db')  # Подключаемся к БД или создает БД (если ее нет)
    cur = base.cursor()  # Создаем курсор
    if base:
        print('\nData base zakaz connected!')
    base.execute(
        'CREATE TABLE IF NOT EXISTS zakaz(id TEXT, name TEXT, numb TEXT, photo, telephone TEXT, dost TEXT)')
    base.commit()  # Сохранен


"""Сохраняем изменения в базе данных"""
async def sql_add_admin_command(state):
    async with state.proxy() as data:  # Открываем словарь
        cur.execute('INSERT INTO album VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_add_zakaz_command(ID, db_name, number, photo, telephone, dost):
    cur.execute('INSERT INTO zakaz VALUES (?, ?, ?, ?, ?, ?)', (ID, db_name, number, photo, telephone, dost))
    base.commit()

"""Читаем и отправляем сообщением базу данных"""

async def sql_read_admin(message):
    for ret in cur.execute('SELECT * FROM album').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'Номер букета: {ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]} BYN')

async def sql_read_zakaz(message):
    for ret in cur.execute('SELECT * FROM zakaz').fetchall():
        if ret[3] == None:
            await bot.send_message(message.from_user.id,
                                 f'<b>ID:</b> {ret[0]}\n<b>Имя:</b> {ret[1]}\n<b>Номер букета:</b> {ret[2]}\n<b>Телефон</b>: {ret[4]},'
                                 f'\n<b>Доставка:</b> {ret[-1]}', parse_mode=types.ParseMode.HTML)
        else:
            await bot.send_photo(message.from_user.id, ret[3], f'<b>ID:</b> {ret[0]}\n<b>Имя:</b> {ret[1]}'
                                                               f'\n<b>Номер букета:</b> Фото\n<b>Телефон:</b> {ret[4]},'
                                                               f'\n<b>Доставка:</b> {ret[-1]}',
                                 parse_mode=types.ParseMode.HTML)
