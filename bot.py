from telegram.ext import Updater, MessageHandler, Filters
from telegram import BotCommand
import re

# Define your bot token here
TOKEN = '6873076181:AAEDQa0jwEFLzqE8nJxuLt5tTW73rD4ZFAw'

# Define your link regex pattern
link_pattern = re.compile(r'https?://\S+')

# Define a function to delete messages with links in user's bio
def delete_messages_with_links(update, context):
    user = update.effective_user
    if user and user.username:
        bio_photos = context.bot.get_user_profile_photos(user.id).photos
        for photo in bio_photos:
            if photo.caption:
                for text in photo.caption.split('\n'):
                    if link_pattern.search(text):
                        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)
                        break

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add message handler to filter messages with links in user's bio
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), delete_messages_with_links))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
