from wfapi import Workflowy
from telegram import ParseMode

import config
from utils import restricted


@restricted
def workflowy_inbox_handler(update, context):
    chat_id = update.effective_chat.id
    message = update.message.text

    wf = Workflowy(sessionid=config.WORKFLOWY_SESSION_ID)

    inbox_node = wf.main.find_node(config.WORKFLOWY_NODE_UUID)

    message_node = inbox_node.create()
    message_node.edit(message)

    success_message = f"✅ Додано в Inbox\! [Переглянути]({config.WORKFLOWY_INBOX_URI})"
    context.bot.send_message(chat_id=chat_id, text=success_message, parse_mode=ParseMode.MARKDOWN_V2)
