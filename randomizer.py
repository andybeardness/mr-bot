import random
import config

def is_need_to_send_message():
	random_value = random.randint(0, config.REPLY_CHANCE)
	if (random_value == 0):
		return True
	else:
		return False