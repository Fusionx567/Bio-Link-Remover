from telegram import Update, ParseMode
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with the actual token of your bot
TOKEN = '6873076181:AAEDQa0jwEFLzqE8nJxuLt5tTW73rD4ZFAw'

def delete_and_warn(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    user_id = user.id

    # Retrieve user profile photos
    profile_photos = context.bot.get_user_profile_photos(user_id)

    # Check if there are any profile photos (indicating a link in bio)
    if profile_photos.photos:
        # User has a link in bio, delete the message
        context.bot.delete_message(update.message.chat_id, update.message.message_id)

        # Send a warning message to the user
        warning_message = "Please remove the link from your bio to avoid message deletion."
        context.bot.send_message(user_id, warning_message, parse_mode=ParseMode.MARKDOWN)

def main():
    # Create an updater and pass it the bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register MessageHandler to check for messages and apply the delete_and_warn function
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, delete_and_warn))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
