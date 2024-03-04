import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('6442848831:AAGqdJG-s_9mL9kG5aCAsuwtvgnpZzMxuPU')

@bot.message_handler(content_types=['text'])
def check_bio(message):
    # Get user's profile photos
    photos = bot.get_user_profile_photos(message.from_user.id)
    # Check if user has any profile photos
    if photos.photos:
        # Extract bio from the first photo
        bio = photos.photos[0][0].file_id
        # Check if the bio contains a link
        if 'http' in bio:
            # Send a warning message to the user
            bot.send_message(message.chat.id, "Please remove the link from your bio.")
            # Delete the message
            bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    else:
        bot.send_message(message.chat.id, "You don't have a profile photo set, I can't check your bio.")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot is active! I will monitor user bios for links.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "This bot checks user bios for links and sends a warning if found.")

if __name__ == '__main__':
    bot.polling()
