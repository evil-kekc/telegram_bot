from aiogram.utils import executor
from create_bot import dp
from data_base import sqlite_db



async def on_startup(_):
    print('Бот вышел в онлайн')
    sqlite_db.sql_start()  # Подключение к базе данных
    sqlite_db.sql_start_1()




from handlers import client, admin, zakaz, other


client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
zakaz.register_handlers_zakaz(dp)
other.register_handlers_other(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  # skip_updates пропускает сообщения, отправленные при выключенном боте