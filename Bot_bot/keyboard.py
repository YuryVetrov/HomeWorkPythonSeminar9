from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
 
######################################################
start = types.ReplyKeyboardMarkup(resize_keyboard=True) # СОЗДАЕМ ВООБЩЕ ОСНОВУ ДЛЯ КНОПОК
 
info = types.KeyboardButton("Информация")            # ДОБАВЛЯЕМ КНОПКУ ИНФОРМАЦИИ
stats = types.KeyboardButton("Статистика")            # ДОБАВЛЯЕМ КНОПКУ СТАТИСТИКИ 
razrab = types.KeyboardButton("Разработчик")            # ДОБАВЛЯЕМ КНОПКУ РАЗРАБОТЧИК
menu = types.KeyboardButton("Меню") 
start.add(menu)
start.add(stats, info) #ДОБАВЛЯЕМ ИХ В БОТА
start.add(razrab)
######################################################
 
stats = InlineKeyboardMarkup()    # СОЗДАЁМ ОСНОВУ ДЛЯ ИНЛАЙН КНОПКИ
stats.add(InlineKeyboardButton(f'Да', callback_data = 'join')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
stats.add(InlineKeyboardButton(f'Нет', callback_data = 'cancle')) # СОЗДАЁМ КНОПКУ И КАЛБЭК К НЕЙ
 