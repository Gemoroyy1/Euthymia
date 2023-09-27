import os
from dotenv import load_dotenv
from telegram.ext import *

# Просто в самом начале все значения из .env здесь же возьмем и дальше будем использовать упрощенно без os.getenv()
load_dotenv()
token=os.getenv('TELEGRAM_TOKEN')

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
