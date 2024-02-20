from telegram.ext import Updater, MessageHandler, Filters
import re

# Replace 'your_bot_token_here' with your actual bot token
TOKEN = '6873076181:AAEDQa0jwEFLzqE8nJxuLt5tTW73rD4ZFAw'

# Define your link regex pattern
link_pattern = re.compile(r'https?://\S+')

# Define a function to delete messages with links in user's bio
def delete_messages_with_links(update, context):
    user = update.effective_user
    if user and user.username and user.description and link_pattern.search(user.description):
        context.bot.delete_message(chat_id=update.effective_chat.id, message_id=update.message.message_id)

def main():
    # Create an Updater and pass it your bot's token
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add message handler to filter messages with links in user's bio
    dp.add_handler(MessageHandler(Filters.text & (~Filters.command), delete_messages_with_links))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop it
    updater.idle()

if __name__ == '__main__':
    main()
