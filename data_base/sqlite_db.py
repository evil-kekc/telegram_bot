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
    base = sq.connect('vsemcveti.db')
    cur = base.cursor()
    if base:
        print('\nData base zakaz connected!')
    base.execute(
        'CREATE TABLE IF NOT EXISTS zakaz(A TEXT PRIMARY KEY, B TEXT, C TEXT)')
    base.commit()  # Сохранен


"""Сохраняем изменения в базе данных"""
async def sql_add_admin_command(state):
    async with state.proxy() as data:  # Открываем словарь
        cur.execute('INSERT INTO album VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()

async def sql_add_zakaz_command(state):
    async with state.proxy() as data:  # Открываем словарь
        cur.execute('INSERT INTO zakaz VALUES (?, ?, ?, ?, ?)', tuple(data.values()))
        base.commit()

"""Читаем и отправляем сообщением базу данных"""

async def sql_read_admin(message):
    for ret in cur.execute('SELECT * FROM album').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'Номер букета: {ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]} BYN')

async def sql_read_zakaz(message):
    for ret in cur.execute('SELECT * FROM zakaz').fetchall():
        await bot.send_photo(message.from_user.id, f'ID: {ret[0]}\n Имя: {ret[1]}\nФамилия: {ret[2]}\nТелефон: {ret[3]}\nЦена: {ret[-1]} BYN')