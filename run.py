from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import config
from handlers.file_uploader import file_uploader_handler
from handlers.workflowy_inbox_handler import workflowy_inbox_handler
from handlers.ping import ping

updater = Updater(token=config.TELEGRAM_TOKEN, use_context=True)

dispatcher = updater.dispatcher

handlers = [
    CommandHandler('ping', ping),
    MessageHandler(Filters.photo | Filters.document, file_uploader_handler),
    MessageHandler(Filters.text, workflowy_inbox_handler)
]

for handler in handlers:
    dispatcher.add_handler(handler)

updater.start_polling()
