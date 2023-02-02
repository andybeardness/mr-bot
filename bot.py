import telebot
import secrets
import randomizer
import reply_manager

bot = telebot.TeleBot(secrets.TOKEN, parse_mode=None)

CONTENT_TYPES = [
	"text", 
	"audio", 
	"document", 
	"photo", 
	"sticker", 
	"video", 
	"video_note", 
	"voice", 
	"location", 
	"contact", 
	"new_chat_members", 
	"left_chat_member", 
	"new_chat_title", 
	"new_chat_photo", 
	"delete_chat_photo",
	"group_chat_created", 
	"supergroup_chat_created", 
	"channel_chat_created", 
	"migrate_to_chat_id",
	"migrate_from_chat_id", 
	"pinned_message",
]

@bot.message_handler(content_types=CONTENT_TYPES)
def reply(message):
	is_need_to_send_message = randomizer.is_need_to_send_message()

	if not is_need_to_send_message:
		return

	reply_message = reply_manager.get_reply()
	bot.reply_to(message, reply_message)

print("Bot start")
bot.infinity_polling()