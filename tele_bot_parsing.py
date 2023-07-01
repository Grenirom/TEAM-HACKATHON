import telebot
from telebot import types
from bs4 import BeautifulSoup
from requests import get

# from my_token import token

bot = telebot.TeleBot('6184082580:AAED8O9jnH6Fjw2QkCDwJ3HAA1qm4n7vis4')

markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = types.KeyboardButton('/start')
btn2 = types.KeyboardButton('Каталог')
markup.add(btn1, btn2)


@bot.message_handler(commands=['start', 'text'])
def start_message(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Нажмините на кнопку каталог', reply_markup=markup)
    bot.register_next_step_handler(msg, find_the_song)


def find_the_song(message):
    url = f'https://ecoland.kg/product/voda-legenda-shoro-1500-ml/'
    html = get_html(url)
    soup = get_soup(html)
    try:
        container = soup.find('div', class_='mega_menu').find('ul')
    except:
        chat_id = message.chat.id
        bot.send_message(chat_id, 'Ничего не нашли')
        start_message(message)
        return
    else:
        all_cats = get_data_songs(container)
        chat_id = message.chat.id
        msg_list = []
        for i in all_cats:
            cat = i['kat']
            link = i['link']
            msg = f'Название категория: "{cat}"\nCсылка {link}\n\n'
            msg_list.append(msg)
        all_msg = ''.join(msg_list)
        bot.send_message(chat_id, all_msg)


def get_html(url: str) -> str:
    '''Эта функция получает HTML разметку по определенному сайту по URL'''
    response = get(url)
    return response.text


def get_soup(html: str) -> BeautifulSoup:
    ''' Получает html разметку и структурирует ее в красивый bs'''
    soup = BeautifulSoup(html, 'lxml')
    return soup


def get_data_songs(container):
    res_search = []
    items = container.find_all('li', class_='mega_menu_item mega_menu_item_has_children')
    for item in items:
        link = item.find('a').get('href')
        kat = item.find('a').text
        data = {
            'kat': kat,
            'link': link
        }
        res_search.append(data)

    return res_search


def no_search_result(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'Уточни запрос. Начнем сначала!')
    start_message()


bot.polling(none_stop=True, interval=0)