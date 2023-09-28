import os
import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv
from telegram.ext import *

load_dotenv()
token=os.getenv('TOKEN')
user=os.getenv('USER')
password=os.getenv('PASSWORD')
host=os.getenv('HOST')
port=os.getenv('PORT')
database=os.getenv('DATABASE')

connection=0

try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(dbname=database, user=user, password=password)

    # Курсор для выполнения операций с базой данных
    cursor = connection.cursor()
    # Распечатать сведения о PostgreSQL
    print("Информация о сервере PostgreSQL")
    print(connection.get_dsn_parameters(), "\n")
    # Выполнение SQL-запроса
    cursor.execute("SELECT version();")
    # Получить результат
    record = cursor.fetchone()
    print("Вы подключены к - ", record, "\n")

    # Выполнение SQL-запроса
    quest='''SELECT * FROM public.test_table
                ORDER BY id ASC '''
    cursor.execute(quest)
    # Получить результат
    record = cursor.fetchone()
    print(record, "\n")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

async def start_command(update, context):
    # Отправляем приветственное сообщение пользователю
    await update.message.reply_text('Привет! Я - Эвтюмия. Я знаю всё, что тебе нужно. \nПо запросу /read я предложу тебе'
                                    ' заглянуть в базу данных мануфактуры, а по запросу /upload я предложу тебе загрузить'
                                    ' новые файлы туда.')
async def upload_command(update, context):
    await update.message.reply_text('Это была команда /upload')

async def read_command(update, context):
    await update.message.reply_text('Это была команда /read')

if __name__=='__main__':
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler('start',start_command))
    application.add_handler(CommandHandler('upload', upload_command))
    application.add_handler(CommandHandler('read', read_command))
    application.run_polling(1.0)
