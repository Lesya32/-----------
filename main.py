import requests, telebot
from datetime import datetime
from auth_data import token


def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nСтоимость валюты: {sell_price}")

def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=['start'])
    def start_message(massage):
        bot.send_message(massage.chat.id, 'Привет')

    @bot.message_handler(content_types=['text'])
    def send_text(massage):
        if massage.text.lower() == "price":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(
                    massage.chat.id,
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nСтоимость валюты: {sell_price}"
                )

            except Exception as ex:
                print(ex)
                bot.send_message(massage.chat.id, 'Ошибка')
        else:
            bot.send_message(massage.chat.id, 'Бот не понимает такие команды, введите price')

    bot.polling()

if __name__ =='__main__':
    get_data()
    telegram_bot(token)