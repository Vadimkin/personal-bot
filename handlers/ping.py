def ping(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Pong")
