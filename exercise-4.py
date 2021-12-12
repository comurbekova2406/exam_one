import telebot

TOKEN = '5004258879:AAE21h6BXOqo5QKC74Pp6lhAdzMMwdtskic'

bot = telebot.TeleBot(TOKEN)
VOWELS_LETTERS = ('е', 'у', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю', 'ё')


@bot.message_handler(func=lambda message: True)
def search_char(message):
    message_text = message.text
    vowels_count = 0

    for char in message_text:
        if char.lower() in VOWELS_LETTERS:
            vowels_count+=1

    bot.reply_to(message,f'Количество гласных букв; {vowels_count}')


bot.infinity_polling()