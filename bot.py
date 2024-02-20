from pyrogram import Client, filters
from pyrogram.types import Message, ChatMemberUpdated

# Your Telegram API credentials
api_id = "21007450"
api_hash = "b86c382f42b509d911c7bca27855754f"
bot_token = "your_bot_token"

# Your private channel chat ID
private_channel_chat_id = -1001848459006  # Replace with your actual private channel chat ID

# Create a Pyrogram Client
app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

# Function to check if a user's bio contains a link
async def has_link(user):
    # Check if the user object is not None and is a bot
    if user is not None and user.is_bot:
        # Fetch the complete ChatMember object using await
        chat_member = await app.get_chat_member(chat_id=private_channel_chat_id, user_id=user.id)

        # Check if the chat_member has a user object and a bio attribute
        if chat_member and hasattr(chat_member.user, 'bio'):
            return "http" in chat_member.user.bio.lower() or "www" in chat_member.user.bio.lower()

    return False

# Event handler for the on_message event
@app.on_message(filters.chat(private_channel_chat_id) & filters.new_chat_members)
async def on_message_handler(client, message: Message):
    # Check if the new chat member is a bot
    for member in message.new_chat_members:
        if member.is_bot:
            # Call the asynchronous has_link function with await
            if await has_link(member):
                # Delete the message if the bot has a link
                await message.delete()

# Event handler for the bot starting
@app.on_startup()
async def on_startup_handler():
    print("Bot has started!")

# Start the bot
app.run()
