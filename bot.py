from pyrogram import Client, filters
from pyrogram.types import Message, ChatMemberUpdated

# Your Telegram API credentials
api_id = "21007450"
api_hash = "b86c382f42b509d911c7bca27855754f"
bot_token = "6873076181:AAEDQa0jwEFLzqE8nJxuLt5tTW73rD4ZFAw"

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

# Function to check and delete messages with links
async def check_and_delete_links(client, message: Message):
    # Check if the message is from a user and contains text
    if message.from_user and message.text:
        # Call the asynchronous has_link function with await
        if await has_link(message.from_user):
            # Delete the message if it has a link
            await message.delete()

# Event handler for the on_chat_member event
@app.on_chat_member(filters.chat(private_channel_chat_id) & filters.incoming & filters.chat_action("joined"))
async def on_chat_member_handler(_, chat_member: ChatMemberUpdated):
    print(f"Bot joined the chat: {chat_member}")

    # Start the message handler
    app.add_handler(check_and_delete_links)

# Start the bot
app.run()
