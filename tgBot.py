import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

TOKEN = 'TELEGRAM_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

admins_chat_ids = [1186961151] 

order_number = 1

user_data = {}

# Шаги бота
STEPS = {
    'MENU': 1,
    'CATEGORY': 2,
    'DRINK': 3,
    'SIZE': 4,
    'MILK': 5,
    'SYRUP': 6,
    'ADDONS': 7,
    'COMMENT': 8,
    'SUMMARY': 9,
    'PAYMENT': 10,
    'RAF_VARIETY': 11
}

# Меню напитков
DRINKS = {
    'hot': ['Эспрессо',
            'Флэт уайт',
            'Американо',
            'Капучино',
            'Латте',
            'Латте солёная карамель',
            'Какао',
            'Матча Латте',
            'Раф'],
    'cold': ['Редбул арбуз',
             'Айс Бамб',
             'Правда кофе',
             'Персиковый чай',
             'Сливочный американо',
             'Тай кофе',
             'Травяной лимонад',
             'Молочный цитрусовый чай',
             'Тропиканка',
             'Матча тоник',
             'Аммерикано крем сода',
             'Эспреccо тоник',
             'Айс матча латте',
             'Айс капучино',
             'Айс американо']
}

# Стоимость
PRICES = {
    'Эспрессо': 100,
    'Американо': 0,
    'Капучино': 0,
    'Латте': 0,
    'Латте солёная карамель': 50,
    'Флэт уайт': 120,
    'Какао': 50,
    'Матча Латте': 50,
    'Раф': 50,
    'Редбул арбуз': 50,
    'Айс Бамб': 50,
    'Правда кофе': 50,
    'Персиковый чай': 50,
    'Сливочный американо': 50,
    'Тай кофе': 50,
    'Травяной лимонад': 50,
    'Молочный цитрусовый чай': 50,
    'Тропиканка': 50,
    'Матча тоник': 50,
    'Аммерикано крем сода': 50,
    'Эспреccо тоник': 50,
    'Айс матча латте': 50,
    'Айс капучино': 50,
    'Айс американо': 50
}

# Объёмы напитков
VOLUMES = {
    'Эспрессо': ['250 мл'],
    'Флэт уайт': ['250 мл'],
    'Американо': ['250 мл', '350 мл', '450 мл', '550 мл'],
    'Капучино': ['250 мл', '350 мл', '450 мл', '550 мл'],
    'Латте': ['350 мл', '450 мл', '550 мл'],
    'Латте солёная карамель': ['350 мл', '450 мл', '550 мл'],
    'Какао': ['350 мл', '450 мл', '550 мл'],
    'Матча Латте': ['350 мл', '450 мл', '550 мл'],
    'Раф': ['350 мл', '450 мл', '550 мл'],
    'Раф (Классический)': ['350 мл', '450 мл', '550 мл'],
    'Раф (Малиновый)': ['350 мл', '450 мл', '550 мл'],
    'Раф (Лавандовый)': ['350 мл', '450 мл', '550 мл'],
    'Раф (Апельсиновый)': ['350 мл', '450 мл', '550 мл'],
    'Эспреccо тоник': ['350 мл', '450 мл', '550 мл'],
    'Матча тоник': ['350 мл', '450 мл', '550 мл'],
    'Правда кофе': ['450 мл'],
    'Тай кофе': ['350 мл', '450 мл', '550 мл'],
    'Аммерикано крем сода': ['350 мл', '450 мл', '550 мл'],
    'Айс Бамб': ['550 мл'],
    'Травяной лимонад': ['350 мл', '450 мл', '550 мл'],
    'Тропиканка': ['350 мл', '450 мл', '550 мл'],
    'Сливочный американо': ['350 мл', '450 мл', '550 мл'],
    'Персиковый чай': ['350 мл', '450 мл', '550 мл'],
    'Молочный цитрусовый чай': ['350 мл', '450 мл', '550 мл'],
    'Айс матча латте': ['550 мл'],
    'Айс капучино': ['550 мл'],
    'Айс американо': ['550 мл'],
    'Редбул арбуз': ['450 мл'],
}

# Цены за выбор объёма
VOLUMES_PRICES= {
    '250 мл': 0,
    '350 мл': 160,
    '450 мл': 220,
    '550 мл': 250,
}

# Выбор молока
MILKS = {
    'Эспрессо': ['Нет молока', 'Обычное молоко', 'Кокосовое', 'Миндальное', 'Овсяное', 'Банановое', 'Ванильное', 'Соевое'],
    'Флэт уайт': ['Обычное молоко', 'Кокосовое', 'Миндальное', 'Овсяное', 'Банановое', 'Ванильное', 'Соевое'],
    'Американо': ['Нет молока'],
    'Капучино': ['Обычное молоко', 'Кокосовое', 'Миндальное', 'Овсяное', 'Банановое', 'Ванильное', 'Соевое'],
    'Латте': ['Обычное молоко', 'Кокосовое', 'Миндальное', 'Овсяное', 'Банановое', 'Ванильное', 'Соевое'],
    'Латте солёная карамель': ['Обычное молоко', 'Кокосовое', 'Миндальное', 'Овсяное', 'Банановое', 'Ванильное', 'Соевое'],
    'Какао': ['Обычное молоко', 'Кокосовое', 'Миндальное', 'Овсяное', 'Банановое', 'Ванильное', 'Соевое'],
    'Матча Латте': ['Обычное молоко', 'Кокосовое', 'Миндальное', 'Овсяное', 'Банановое', 'Ванильное', 'Соевое'],
    'Раф': ['Обычное молоко и сливки'],
    'Эспреccо тоник': ['Нет молока'],
    'Матча тоник': ['Нет молока'],
    'Правда кофе': ['Нет молока'],
    'Тай кофе': ['Обычное молоко', 'Кокосовое', 'Миндальное', 'Овсяное', 'Банановое', 'Ванильное', 'Соевое'],
    'Аммерикано крем сода': ['Нет молока'],
    'Айс Бамб': ['Нет молока'],
    'Травяной лимонад': ['Нет молока'],
    'Тропиканка': ['Нет молока'],
    'Сливочный американо': ['Нет молока'],
    'Персиковый чай': ['Нет молока'],
    'Молочный цитрусовый чай': ['Обычное молоко', 'Кокосовое', 'Миндальное', 'Овсяное', 'Банановое', 'Ванильное', 'Соевое'],
    'Айс раф': ['Обычное молоко и сливки'],
    'Айс матча латте': ['Обычное молоко', 'Кокосовое', 'Миндальное', 'Овсяное', 'Банановое', 'Ванильное', 'Соевое'],
    'Айс капучино': ['Обычное молоко', 'Кокосовое', 'Миндальное', 'Овсяное', 'Банановое', 'Ванильное', 'Соевое'],
    'Айс американо': ['Нет молока', 'Обычное молоко', 'Кокосовое', 'Миндальное', 'Овсяное', 'Банановое', 'Ванильное', 'Соевое'],
    'Редбул арбуз': ['Нет молока'],
    'Раф (Классический)': ['Обычное молоко и сливки'],
    'Раф (Малиновый)': ['Обычное молоко и сливки'],
    'Раф (Лавандовый)': ['Обычное молоко и сливки'],
    'Раф (Апельсиновый)': ['Обычное молоко и сливки']
}
# Цены за выбор молока
MILK_PRICES = {
    'Нет молока': 0,
    'Обычное молоко': 0,
    'Кокосовое': 90,
    'Миндальное': 90,
    'Овсяное': 90,
    'Банановое': 90,
    'Ванильное': 90,
    'Соевое': 90
}

# Цены за выбор сиропов
SYRUPS = ['Ваниль', 'Карамель','Солёная карамель', 'Халва', 'Шоколад', 'Лаванда', 'Лесной орех', 'Фисташка', 'Кокос', 'Ежевика', 'Малина', 'Апельсин', 'Груша', 'Манго', 'Без сиропа']

SYRUP_PRICES = {
    'Ваниль': 20,
    'Карамель': 20,
    'Солёная карамель': 20,
    'Халва': 20,
    'Шоколад': 20,
    'Лаванда': 20,
    'Лесной орех': 20,
    'Фисташка': 20,
    'Кокос': 20,
    'Ежевика': 20,
    'Малина': 20,
    'Апельсин': 20,
    'Груша': 20,
    'Манго': 20,
    'Без сиропа': 0
}

# Цены за выбор добавок
ADDONS = ['Дополнительный эспрессо', 'Сгущённое молоко', 'Топиннг (солёная карамель)', 'Маршмеллоу', 'Взбитые сливки', 'Без добавок']

NO_ADDONS_DRINKS = ['Эспрессо', 'Ред Булл', 'Правда кофе']

ADDON_PRICES = {
    'Дополнительный эспрессо': 50,
    'Сгущённое молоко': 30,
    'Топиннг (солёная карамель)': 30,
    'Маршмеллоу': 30,
    'Взбитые сливки': 30,
    'Без добавок': 0
}

# Новый выбор для Раф
RAF_SYRUPS = ['Малиновый', 'Классический', 'Лавандовый', 'Апельсиновый']

DRINKS_DESCRIPTION = {
    'Эспрессо': 'Насыщенный кофейный напиток',
    'Флэт уайт': 'Кофейный напиток на основе эспрессо',
    'Американо': 'Классический кофейный напиток',
    'Капучино': 'Молочный кофейный напиток',
    'Латте': 'Лёгкий молочно-кофейный напиток',
    'Латте солёная карамель': 'Кофейный напиток с солёной карамелью',
    'Какао': 'Классический напиток на основе какао',
    'Матча Латте': 'Японский чай',
    'Раф': 'Нежный сливочный кофейный напиток',
    'Персиковый чай': 'Фруктовый чайный напиток',
}

def start_order(user_id):
    user_data[user_id] = {
        'step': STEPS['MENU'],
        'previous_steps': [],
        'order': {}
    }
    bot.send_message(user_id, "Здравствуйте! Вас приветствует Правда бот. Наша кофейня находится по адресу: Тверска 20/1 ст1.")
    show_menu(user_id)

def show_menu(user_id):
    markup = InlineKeyboardMarkup()
    hot_button = InlineKeyboardButton("Горячие напитки", callback_data="category_hot")
    cold_button = InlineKeyboardButton("Холодные напитки", callback_data="category_cold")
    markup.add(hot_button, cold_button)
    bot.send_message(user_id, "Выберите категорию напитков:", reply_markup=markup)

def show_drinks(user_id, category):
    user_data[user_id]['order']['category'] = category
    markup = InlineKeyboardMarkup()
    for drink in DRINKS[category]:
        markup.add(InlineKeyboardButton(drink, callback_data=f"drink_{drink}"))
    markup.add(InlineKeyboardButton("Назад", callback_data="back"))
    bot.send_message(user_id, "Выберите напиток:", reply_markup=markup)

def show_sizes(user_id, drink):
    user_data[user_id]['order']['drink'] = drink
    markup = InlineKeyboardMarkup()
    for size in VOLUMES[drink]:
        markup.add(InlineKeyboardButton(size, callback_data=f"size_{size}"))
    markup.add(InlineKeyboardButton("Описание напитка", callback_data="description"))
    markup.add(InlineKeyboardButton("Назад", callback_data="back"))
    bot.send_message(user_id, "Выберите размер напитка:", reply_markup=markup)

def show_milks(user_id, drink):
    markup = InlineKeyboardMarkup()
    for milk in MILKS[drink]:
        markup.add(InlineKeyboardButton(milk, callback_data=f"milk_{milk}"))
    markup.add(InlineKeyboardButton("Назад", callback_data="back"))
    bot.send_message(user_id, "Выберите тип молока:", reply_markup=markup)

def show_syrups(user_id):
    markup = InlineKeyboardMarkup()
    for syrup in SYRUPS:
        markup.add(InlineKeyboardButton(syrup, callback_data=f"syrup_{syrup}"))
    markup.add(InlineKeyboardButton("Назад", callback_data="back"))
    bot.send_message(user_id, "Выберите сироп:", reply_markup=markup)

def show_addons(user_id):
    markup = InlineKeyboardMarkup()
    for addon in ADDONS:
        markup.add(InlineKeyboardButton(addon, callback_data=f"addon_{addon}"))
    markup.add(InlineKeyboardButton("Назад", callback_data="back"))
    bot.send_message(user_id, "Выберите дополнения:", reply_markup=markup)

def offer_water(user_id):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Да", callback_data="water_yes"))
    markup.add(InlineKeyboardButton("Нет", callback_data="water_no"))
    bot.send_message(user_id, "Вы хотите добавить воду к вашему эспрессо?", reply_markup=markup)

def show_comment_request(user_id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Добавить комментарий", callback_data="add_comment"),
               InlineKeyboardButton("Нет", callback_data="no_comment"))
    bot.send_message(user_id, "Хотите добавить комментарий к заказу?", reply_markup=markup)


def callback_inline(call):
    if call.data == "add_comment":
        bot.send_message(call.message.chat.id, "Пожалуйста, введите ваш комментарий:")
        bot.register_next_step_handler(call.message, save_comment)
    elif call.data == "no_comment":
        show_summary(call.message)

def save_comment(message):
    user_data[message.chat.id]['comment'] = message.text
    show_summary(message)

def show_summary(user_id):
    order = user_data[user_id]['order']
    summary = "Ваш заказ:\n"
    summary += f"Категория: {order.get('category', '')}\n"
    summary += f"Напиток: {order.get('drink', '')}\n"
    summary += f"Размер: {order.get('size', '')}\n"
    summary += f"Молоко: {order.get('milk', '')}\n"
    summary += f"Сироп: {order.get('syrup', '')}\n"
    summary += f"Дополнения: {order.get('addon', '')}\n"
    summary += f"Комментарий: {order.get('comment', 'Нет комментария')}\n"
    summary += f"Итого: {calculate_total(order)} руб.\n"
    summary += f"При оплате через бота, возврат средств не предусмотрен.\n"
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Оплатить", callback_data="confirm"))
    markup.add(InlineKeyboardButton("Назад", callback_data="back"))
    bot.send_message(user_id, summary, reply_markup=markup)

def calculate_total(order):
    total = PRICES.get(order.get('drink', ''), 0)
    total += VOLUMES_PRICES.get(order.get('size', ''), 0)
    total += MILK_PRICES.get(order.get('milk', ''), 0)
    total += SYRUP_PRICES.get(order.get('syrup', ''), 0)
    total += ADDON_PRICES.get(order.get('addon', ''), 0)
    return total

def go_back(user_id):
    if user_data[user_id]['previous_steps']:
        user_data[user_id]['step'] = user_data[user_id]['previous_steps'].pop()
        show_step(user_id)

def show_step(user_id):
    step = user_data[user_id]['step']
    if step == STEPS['MENU']:
        show_menu(user_id)
    elif step == STEPS['CATEGORY']:
        show_drinks(user_id, user_data[user_id]['order']['category'])
    elif step == STEPS['DRINK']:
        show_sizes(user_id, user_data[user_id]['order']['drink'])
    elif step == STEPS['SIZE']:
        show_milks(user_id, user_data[user_id]['order']['drink'])
    elif step == STEPS['MILK']:
        show_syrups(user_id)
    elif step == STEPS['SYRUP']:
        show_addons(user_id)
    elif step == STEPS['ADDONS']:
        show_summary(user_id)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    user_id = call.from_user.id
    if user_id not in user_data:
        start_order(user_id)
        return

    if call.data.startswith("category_"):
        category = call.data.split("_")[1]
        user_data[user_id]['previous_steps'].append(user_data[user_id]['step'])
        user_data[user_id]['step'] = STEPS['CATEGORY']
        show_drinks(user_id, category)
    elif call.data.startswith("drink_"):
        drink = call.data.split("_")[1]
        user_data[user_id]['previous_steps'].append(user_data[user_id]['step'])
        user_data[user_id]['step'] = STEPS['DRINK']
        show_sizes(user_id, drink)
    elif call.data.startswith("size_"):
        size = call.data.split("_")[1]
        user_data[user_id]['order']['size'] = size
        user_data[user_id]['previous_steps'].append(user_data[user_id]['step'])
        user_data[user_id]['step'] = STEPS['SIZE']
        drink = user_data[user_id]['order']['drink']
        if drink == 'Эспрессо':
            offer_water(user_id)
        else:
            show_milks(user_id, drink)
    elif call.data == "water_yes":
        user_data[user_id]['order']['water'] = 'Да'
        show_milks(user_id, user_data[user_id]['order']['drink'])
    elif call.data == "water_no":
        user_data[user_id]['order']['water'] = 'Нет'
        show_milks(user_id, user_data[user_id]['order']['drink'])
    elif call.data.startswith("milk_"):
        milk = call.data.split("_")[1]
        user_data[user_id]['order']['milk'] = milk
        user_data[user_id]['previous_steps'].append(user_data[user_id]['step'])
        user_data[user_id]['step'] = STEPS['MILK']
        show_syrups(user_id)
    elif call.data.startswith("syrup_"):
        syrup = call.data.split("_")[1]
        user_data[user_id]['order']['syrup'] = syrup
        user_data[user_id]['previous_steps'].append(user_data[user_id]['step'])
        user_data[user_id]['step'] = STEPS['SYRUP']
        drink = user_data[user_id]['order']['drink']
        if drink in NO_ADDONS_DRINKS:
            show_comment_request(user_id)
        else:
            show_addons(user_id)
    elif call.data.startswith("addon_"):
        addon = call.data.split("_")[1]
        user_data[user_id]['order']['addon'] = addon
        user_data[user_id]['previous_steps'].append(user_data[user_id]['step'])
        user_data[user_id]['step'] = STEPS['ADDONS']
        show_comment_request(user_id)
    elif call.data == "back":
        go_back(user_id)
    elif call.data == "description":
        drink = user_data[user_id]['order']['drink']
        description = DRINKS_DESCRIPTION.get(drink, "Описание недоступно.")
        bot.send_message(user_id, description)
        show_sizes(user_id, drink)
    elif call.data == "confirm_payment":
        show_summary(user_id)
    elif call.data == "confirm":
        global order_number
        order_number += 1
        bot.send_message(user_id, f"Заказ #{order_number} подтвержден. Ваш кофе будет готов в течении 10 минут, по адресу: Тверская 20/1 ст.1. Ждём вас!")

        order = user_data[user_id]['order']
        order_text = f"Новый заказ #{order_number}:\n"
        order_text += f"Пользователь: {call.from_user.username}\n"
        order_text += f"Категория: {order.get('category', '')}\n"
        order_text += f"Напиток: {order.get('drink', '')}\n"
        order_text += f"Размер: {order.get('size', '')}\n"
        order_text += f"Вода: {order.get('water', 'Нет')}\n"
        order_text += f"Молоко: {order.get('milk', '')}\n"
        order_text += f"Сироп: {order.get('syrup', '')}\n"
        order_text += f"Дополнения: {order.get('addon', '')}\n"
        order_text += f"Комментарий: {order.get('comment', 'Нет комментария')}\n"
        order_text += f"Итого: {calculate_total(order)} руб.\n"
        for admin_chat_id in admins_chat_ids:
            bot.send_message(admin_chat_id, order_text)
        start_order(user_id)

@bot.message_handler(func=lambda message: user_data.get(message.from_user.id, {}).get('step') == STEPS['COMMENT'])
def handle_comment(message):
    user_id = message.from_user.id
    user_data[user_id]['order']['comment'] = message.text
    show_summary(user_id)

@bot.message_handler(commands=['start'])
def handle_start(message):
    start_order(message.from_user.id)

bot.polling()
