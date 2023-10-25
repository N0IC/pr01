import telebot
import config
from extensions import CurrencyConverter, APIException

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    # Обработчик команд /start и /help
    intro_message = 'Привет! Я бот для получения цены валюты. Чтобы получить цену валюты, введи команду /values и укажи исходную и целевую валюты через пробел.'
    bot.send_message(message.chat.id, intro_message)

@bot.message_handler(commands=['values'])
def handle_values(message):
    # Обработчик команды /values
    try:
        # Получаем параметры из сообщения пользователя
        params = message.text.split()[1:]

        if len(params) != 2:
            raise APIException(
                'Неверное количество параметров. Введите команду в формате /values <BASE_CURRENCY> <TARGET_CURRENCY>')

        base_currency = params[0].upper()
        target_currency = params[1].upper()

        # Получаем цену валюты
        price = CurrencyConverter.get_price(base_currency, target_currency)

        # Отправляем ответ пользователю
        response_message = f'1 {base_currency} = {price} {target_currency}'
        bot.send_message(message.chat.id, response_message)

    except APIException as e:
        bot.send_message(message.chat.id, f'Произошла ошибка: {str(e)}')

@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    # Обработчик сообщений от пользователя, отличных от команды
    bot.send_message(message.chat.id, 'Я не понимаю тебя. Для получения помощи введите команду /help.')


# Запуск бота
bot.polling()