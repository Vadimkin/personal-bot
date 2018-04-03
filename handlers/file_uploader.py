import os
import uuid

import config
from utils import get_full_url


def file_handler(bot, update):
    if update.message.document is not None:
        file_id = update.message.document
    elif len(update.message.photo) > 0:
        file_id = update.message.photo[-1]
    else:
        bot.send_message(chat_id=update.message.chat_id, text="Can't recognize type of document")
        return False

    file = bot.get_file(file_id)

    file_extension = file.file_path.split('.')[-1]
    filename = f'{uuid.uuid4()}.{file_extension}'
    file.download(os.path.join(config.IMAGES_UPLOAD_DIR, filename))

    file_url = get_full_url(filename)

    bot.send_message(
        chat_id=update.message.chat_id,
        text=f"Uploaded!\n{file_url}",
        disable_web_page_preview=True
    )
