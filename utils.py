import config


def get_full_url(filename):
    return f'{config.SCREENSHOT_HOST}{filename}'
