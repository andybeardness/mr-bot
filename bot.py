import telebot
import secrets
import randomizer
import reply_manager

bot = telebot.TeleBot(secrets.TOKEN, parse_mode=None)

@bot.message_handler(func=lambda _: True)
def reply(message):
	is_need_to_send_message = randomizer.is_need_to_send_message()

	if not is_need_to_send_message:
		return

	reply_message = reply_manager.get_reply()
	bot.reply_to(message, reply_message)

print("Bot start")
bot.infinity_polling()