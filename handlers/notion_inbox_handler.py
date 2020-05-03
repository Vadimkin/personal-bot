from notion.block import TweetBlock, CalloutBlock
from notion.client import NotionClient
from telegram import ParseMode

import config
from utils import is_url, restricted


@restricted
def notion_inbox_handler(update, context):
    chat_id = update.effective_chat.id
    message = update.message.text

    client = NotionClient(token_v2=config.NOTION_TOKEN)

    inbox_page = client.get_block(config.NOTION_INBOX_URI)

    success_message = f"✅ Додано в #{inbox_page.title_plaintext}\! [Переглянути]({config.NOTION_INBOX_URI})"

    if is_url(message) and message.startswith('https://twitter.com'):
        tweet_url = message.strip()
        tweet = inbox_page.children.add_new(TweetBlock)
        # sets "property.source" to the URL, and "format.display_source" to the embedly-converted URL
        try:
            tweet.set_source_url(tweet_url)
        except KeyError:
            # Sometimes it's KeyError due to URL parsing, but it's error with notion package
            # url = list(BeautifulSoup(data["html"], "html.parser").children)[0]["src"]
            pass

        context.bot.send_message(chat_id=chat_id, text=success_message, parse_mode=ParseMode.MARKDOWN_V2)
        return

    text_block = inbox_page.children.add_new(CalloutBlock)
    text_block.title = message
    text_block.icon = "🔗" if "https" in message else "💡"

    context.bot.send_message(chat_id=chat_id, text=success_message, parse_mode=ParseMode.MARKDOWN_V2)
