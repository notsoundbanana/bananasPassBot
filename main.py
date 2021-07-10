import telebot
import pass_generator

bot = telebot.TeleBot("1876463567:AAFLL5wMv8auiHzy1QKieA91BY0Z3MoDGI0")

length = 0


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Hello!")


@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == '/generate':
        bot.send_message(message.from_user.id, "Length?")
        bot.register_next_step_handler(message, generating)
    else:
        bot.send_message(message.from_user.id, 'Write /generate')
    # elif message.text == "/help":
    #     bot.send_message(message.from_user.id, "Напиши привет")
    # else:
    #     bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


def generating(message):
    global length
    try:
        length = int(message.text)
        bot.send_message(message.from_user.id, str(pass_generator.main(int(length))))
    except Exception:
        bot.send_message(message.from_user.id, "Write the length in the range from 8 to 128")
        bot.register_next_step_handler(message, generating)


bot.polling(none_stop=True, interval=0)
