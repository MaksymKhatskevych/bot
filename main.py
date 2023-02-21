from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


load_dotenv(find_dotenv())
# Створення бота
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))

# Обробник команди /start
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    categories_button = KeyboardButton("Категорії")
    info_button = KeyboardButton("Інформація")
    constructors_button = KeyboardButton("Конструктор")
    keyboard.add(categories_button, info_button, constructors_button)
    bot.send_message(message.chat.id, 'Виберіть дію:', reply_markup=keyboard)


bot.polling()
