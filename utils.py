from functools import wraps
from urllib.parse import urlparse

import config


def get_full_url(filename):
    return f'{config.SCREENSHOT_HOST}{filename}'


def is_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id != config.TELEGRAM_GOD_ID:
            context.bot.send_message(user_id, text="JUST. DON'T. DO. IT.")
            context.bot.send_sticker(user_id, config.TELEGRAM_FORBIDDEN_STICKER_ID)

            user = update.effective_user
            user_metadata = f"{user.first_name} {user.last_name} (id{user.id}, @{user.username})"

            message = update.message.text
            context.bot.send_message(config.TELEGRAM_GOD_ID, text=f"Юзер {user_metadata} намагався заюзати бота\n\nMessage: {message}")

            return
        return func(update, context, *args, **kwargs)

    return wrapped
