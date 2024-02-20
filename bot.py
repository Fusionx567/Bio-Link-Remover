from pyrogram import Client, filters
from pyrogram.types import Message

# Your Telegram API credentials
api_id = "21007450"
api_hash = "b86c382f42b509d911c7bca27855754f"
bot_token = "6873076181:AAEDQa0jwEFLzqE8nJxuLt5tTW73rD4ZFAw"

# Create a Pyrogram Client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Dictionary to keep track of users who have been warned
warned_users = {}

# Function to check if a user's bio contains a link
def has_link(user):
    # Check if the user object is not None and is a bot
    if user is not None and user.is_bot:
        # Fetch the complete ChatMember object
        chat_member = app.get_chat_member(chat_id=-1001848459006, user_id=user.id)
        
        # Check if the chat_member has a user object and a bio attribute
        if chat_member and hasattr(chat_member.user, 'bio'):
            return "http" in chat_member.user.bio.lower() or "www" in chat_member.user.bio.lower()
    
    return False

# Function to delete message and warn user
async def delete_and_warn_user(message: Message):
    user_id = message.from_user.id

    # Check if the user has already been warned
    if user_id in warned_users:
        # User has been warned before, delete the message
        await message.delete()
    else:
        # User has not been warned, send a warning message
        await message.reply_text("Please remove the link from your bio. Links are not allowed.")
        
        # Add the user to the warned_users dictionary
        warned_users[user_id] = True

# Command handler for /start
@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    await message.reply_text("Bot is live. Use /check to see if your bio contains a link.")

# Command handler for /check
@app.on_message(filters.command("check"))
async def check_command(client, message: Message):
    user_id = message.from_user.id

    if has_link(message.from_user):
        await message.reply_text("Your bio contains a link. Please remove it.")
    else:
        await message.reply_text("Your bio does not contain a link. You're good!")

# Message handler to check and delete messages with links
@app.on_message(filters.group & filters.text)
async def check_and_delete_links(client, message: Message):
    if has_link(message.from_user):
        await delete_and_warn_user(message)

# Start the bot
app.run()
