import os
import telebot
import gspread
import time
import schedule
import threading
from dotenv import load_dotenv
from telebot import types


load_dotenv()

key_bot = os.getenv("BOT_TOKEN")

leaders_contacts = {
    "Молодіжка": "@ivan_youth",
    "Прославлення": "@anna_worship",
    "Дитяче служіння": "@maria_kids",
    "Домашня група (Центр)": "@oleg_center"
}

gc = gspread.service_account(filename='credentials.json')
sh = gc.open('Church_Schedule')

bot = telebot.TeleBot(key_bot)

worksheet = sh.sheet1

def send_schedule(message):
    data = worksheet.get_all_records()

    response_text = "Наш розклад:\n\n"

    #Перебираємо список у якому декілька словників
    for row in data:
        #Запаковуємо словник на змінні
        day = row["День"]
        service = row["Служіння"]
        time = row["Час"]

        #Формуємо відповідь у вигляді str
        response_text += f"🗓 {day}: {service} о {time}\n"

    bot.send_message(message.chat.id, response_text)


@bot.message_handler(commands=["start"])
def send_start(message):
    # Об'єкт message містить купу корисної інформації:
    # message.chat.id - унікальний ID чату, куди треба відправити відповідь
    # message.from_user.first_name - ім'я людин
    user_name = message.from_user.first_name

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    #Кнопки
    btn1 = types.KeyboardButton("📞 Контакти лідерів")
    btn2 = types.KeyboardButton("📅 Розклад служінь")
    btn3 = None

    #Додавання кнопок
    markup.add(btn1, btn2)

    bot.reply_to(message, f"Привіт {user_name}! Я помічник нашої церкви. Обери команду в меню.", reply_markup=markup)


def send_contacts(message):
    response_text = "Наші контакти:\n\n"

    # Метод .items() віддає одразу два значення: ключ і його значення
    for name, contact in leaders_contacts.items():
        # Додаємо нові дані до нашого тексту (+=) і перехід на новий рядок (\n)
        response_text += f"{name}: {contact}\n"

    bot.send_message(message.chat.id, response_text)

@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "📞 Контакти лідерів":
        send_contacts(message)

    elif message.text == "📅 Розклад служінь":
        send_schedule(message)

    elif message.text == None:
        None

    else:
        bot.send_message(message.chat.id, "оберіть команду")


if __name__ == "__main__":
    print("Бот успішно запущено. Чекаю на повідомлення...")
    # polling означає, що бот постійно "стукає" на сервери Telegram і питає:
    # "Є нові повідомлення? А зараз? А зараз?"
    bot.polling(none_stop=True)