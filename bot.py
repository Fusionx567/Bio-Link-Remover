import telebot

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('YOUR_BOT_TOKEN')

@bot.message_handler(content_types=['text'])
def check_bio(message):
    # Check if the user's bio contains a link
    if 'http' in message.from_user.bio:
        # Send a warning message to the user
        bot.send_message(message.chat.id, "Please remove the link from your bio.")
        # Delete the message
        bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    else:
        # If no link is found, do nothing
        pass

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Bot is active! I will monitor user bios for links.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "This bot checks user bios for links and sends a warning if found.")

if __name__ == '__main__':
    bot.polling()
