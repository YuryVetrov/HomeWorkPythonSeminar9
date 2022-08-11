import logging
from aiogram import Bot, Dispatcher, executor, types
import requests
import datetime


API_TOKEN = '5401746778:AAEJiFNUMsN-J5ecOt_Re23lEJ0sa0M-U3Q'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'menu'])
async def send_welcome(message: types.Message):
    """
    Этот обработчик будет вызываться, когда пользователь отправляет `/start` or `/menu`    
    """
    await message.reply("Привет!\nМеня зовут Pipka_bot!\nЕсли хочешь посмотреть прогноз погоды набери /weather\
                        \nВызвать это меню /menu")
    
@dp.message_handler(commands=["weather"])
async def get_weather1(message: types.Message):
    await message.reply("Привет! Напиши мне город и я скажу тебе какая в нем погода)")

@dp.message_handler()
async def get_weather2(message: types.Message):

     # погодные условия
    weather_conditions = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Little rain \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B"
    }
    #использование «запросов» для импорта данных с сайта погоды
    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={'a5d1dd42647f4afd32d5317bceb4ea64'}&units=metric"
        )
        data = r.json()
        # погодные условия
        weather_description = data["weather"][0]["main"]
        if weather_description in weather_conditions:
            weather_description_answer = weather_conditions[weather_description]
        else:
            weather_description_answer = "Посмотрите на погоду сами)"

        city = data["name"]
        current_weather = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(data["sys"]["sunrise"])

        await message.reply(f"""
            Сегодня {datetime.datetime.now().strftime("%Y-%m-%d")}
            Погода в городе {city}:
            Температура: {current_weather} C°, {weather_description_answer}
            Влажность: {humidity} %
            Давление: {pressure} мм рт.ст.
            Скорость ветра: {wind_speed} м/с
            Восход солнца в: {sunrise_timestamp}
            Закат в: {sunset_timestamp}
            Продолжительность дня: {length_of_the_day}
            Хорошего дня!
            """)
    except Exception as ex:
        await message.reply("Проверьте: правильно ли написано название города?")

if __name__ == '__main__':
    executor.start_polling(dp)