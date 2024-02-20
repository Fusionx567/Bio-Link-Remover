from pyrogram import Client, filters
from pyrogram.types import Message

# Your Telegram API credentials
api_id = "21007450"
api_hash = "b86c382f42b509d911c7bca27855754f"
bot_token = "6873076181:AAEDQa0jwEFLzqE8nJxuLt5tTW73rD4ZFAw"
# Your group chat ID
group_chat_id = -1001848459006  # Replace with your actual group chat ID

# Create a Pyrogram Client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Function to check if a user's bio contains a link
async def has_link(user):
    try:
        # Check if the user is a bot and has a bio attribute
        return user is not None and user.is_bot and hasattr(user, 'bio') and ("http" in user.bio.lower() or "www" in user.bio.lower())
    except Exception as e:
        print(f"Error checking link: {str(e)}")
        return False

# Event handler for the on_message event
@app.on_message(filters.chat(group_chat_id) & filters.all)
async def on_message_handler(client, message: Message):
    try:
        user = message.from_user
        print(f"Received message from user: {user}")
        if await has_link(user):
            # Delete the message if the user has a link in their bio
            await message.delete()
    except Exception as e:
        print(f"Error 

