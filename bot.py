from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a function to handle the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send /groups <user-id> to get the list of groups a user is in.')

# Define a function to handle the /groups command
def groups(update: Update, context: CallbackContext) -> None:
    # Extract the user_id from the command
    user_id = None
    if context.args:
        user_id = context.args[0]

    if not user_id:
        update.message.reply_text('Please provide a user ID. Usage: /groups <user-id>')
        return

    user_groups = []

    # Get the user's member info in each chat
    for chat in context.bot.get_chat(user_id).get_member():
        if chat.status == 'member':
            user_groups.append(chat.link)

    if user_groups:
        groups_text = '\n'.join(user_groups)
        update.message.reply_text(f'The user is in the following groups:\n{groups_text}')
    else:
        update.message.reply_text('The user is not a member of any groups.')

# Define a function to handle errors
def error(update: Update, context: CallbackContext) -> None:
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main() -> None:
    # Create the Updater and pass it your bot's token
    updater = Updater("6873076181:AAEDQa0jwEFLzqE8nJxuLt5tTW73rD4ZFAw")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("groups", groups, pass_args=True))

    # Log all errors
    dispatcher.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
