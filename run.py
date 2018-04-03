from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import config
from handlers.file_uploader import file_handler
from handlers.ping import ping

updater = Updater(token=config.TELEGRAM_TOKEN)

dispatcher = updater.dispatcher

start_handler = CommandHandler('ping', ping)
dispatcher.add_handler(start_handler)

image_handler = MessageHandler(Filters.photo | Filters.document, file_handler)
dispatcher.add_handler(image_handler)

updater.start_polling()
