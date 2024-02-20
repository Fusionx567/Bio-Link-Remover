from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ChatMemberHandler

# Replace 'YOUR_BOT_TOKEN' with the actual token of your bot
TOKEN = '6873076181:AAEDQa0jwEFLzqE8nJxuLt5tTW73rD4ZFAw'

# Dictionary to store user verification status
user_verification_status = {}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Welcome to the group! To verify, click on the captcha link.')

def captcha_handler(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    user_verification_status[user_id] = True
    update.message.reply_text('You are now verified and can participate in the group.')

def check_link_bio(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    user_id = user.id

    if user_id in user_verification_status and user_verification_status[user_id]:
        # User is verified, allow messages
        pass
    else:
        # User is not verified, check bio for links
        if user.link:
            # User has a link in bio, mute and request to remove it
            context.bot.restrict_chat_member(update.message.chat_id, user_id, until_date=None, can_send_messages=False)
            update.message.reply_text("Please remove the link from your bio to participate in the group.")

# Create an updater and pass it the bot's token
updater = Updater(TOKEN)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Register command handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("captcha", captcha_handler))

# Register ChatMemberHandler to handle new users joining the group
dispatcher.add_handler(ChatMemberHandler(check_link_bio, filters=Filters.status_update.new_chat_members))

# Start the Bot
updater.start_polling()
updater.idle()
