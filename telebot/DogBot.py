import configparser
import telebot
import json
import requests

config = configparser.ConfigParser()
config.read('config.ini')
token = config['Telegram']['bot_token']
url = config['Telegram']['url']

bot = telebot.TeleBot(token)


# Обработка команды start
@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, 'Привет! Отправьте фото песеля для определения породы')


# Обработка команды help
@bot.message_handler(commands=['help'])
def send_start(message):
    bot.send_message(message.chat.id, 'Это классификатор пород собакенов. Я знаю 120 пород и помогу Вам '
                                      'определить что за песик изображен на фото. \nПросто отправьте мне изображение')


# Ответ на текстовое сообщение от пользователя
@bot.message_handler(content_types=['text'])
def handle_command(message):
    bot.send_message(message.chat.id, 'Это что-то на кошачьем? Чтобы я мог определить породу собани Вам необходимо '
                                      'отправить фото')


# Обработка отправленного пользователем фото и выдача ответа с предсказанием
@bot.message_handler(content_types=['photo'])
def handle_command(message):
    raw = message.photo[2].file_id
    file_info = bot.get_file(raw)
    downloaded_file = bot.download_file(file_info.file_path)
    try:
        r = requests.post(url + 'predict/', files={'photo': downloaded_file})
        prediction = r.json()
        breed_eng, score = prediction['label'], prediction['score']

        with open('breeds.json', 'r', encoding='utf-8') as f:
            breeds_json = json.load(f)
            breed_ru = breeds_json[breed_eng]

        bot.send_message(message.chat.id, f'''Этот песик относится к породе '{breed_ru}' с вероятностью {score}%''')
        if prediction['score'] < 20:
            bot.send_message(message.chat.id, 'Так как я не могу дать более точного ответа, возможно, '
                                              'на фото не собаня')
    except requests.exceptions.ConnectionError:
        bot.send_message(message.chat.id, 'Прости, но мой рабочий день на сегодня закончен. Но я буду ждать тебя в '
                                          'другое время')


# Запуск бота
bot.infinity_polling()
