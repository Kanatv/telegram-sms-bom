import telebot

bot = telebot.TeleBot('1399499043:AAGSbQx-CLxJ3Ct8o8FS8ICkDnNQbmVXMQ8')


def extract_arg(arg):
    return arg.split()[1]


def extract_arg2(arg2):
    return arg2.split()[2]


@bot.message_handler(commands=['start'])
def start(message):
    start = 'To start SMS Bomber type /bomber number time(in seconds)' \
            '\nFor example /bomber +48123456789 60'
    bot.send_message(message.chat.id, start)


@bot.message_handler(commands=['bomber'])
def bomber(message):
    status = extract_arg(message.text)
    status2 = extract_arg2(message.text)
    time_integer = int(status2)
    time = time_integer
    threads = 4
    target = status
    from SMS.main import SMS_ATTACK
    SMS_ATTACK(threads, time, target)


bot.polling()
