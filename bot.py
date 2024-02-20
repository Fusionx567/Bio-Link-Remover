from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with the actual token of your bot
TOKEN = '6873076181:AAEDQa0jwEFLzqE8nJxuLt5tTW73rD4ZFAw'

def check_link_bio(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    user_id = user.id

    if user.link:
        # User has a link in bio, restrict them from sending messages
        context.bot.restrict_chat_member(update.message.chat_id, user_id, until_date=None, can_send_messages=False)
        update.message.reply_text("Please remove the link from your bio to participate in the group.")
    else:
        # User does not have a link, allow messages
        context.bot.restrict_chat_member(update.message.chat_id, user_id, can_send_messages=True)

def new_member_handler(update: Update, context: CallbackContext) -> None:
    # Handle new members by calling the check_link_bio function
    for member in update.message.new_chat_members:
        check_link_bio(update.message, context)

# Create an updater and pass it the bot's token
updater = Updater(TOKEN)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Register MessageHandler to handle new chat members
dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member_handler))

# Start the Bot
updater.start_polling()
updater.idle()
