import logging 
from aiogram import Bot, Dispatcher, executor, types 
from datetime import datetime
import time

API_TOKEN = '5401746778:AAEJiFNUMsN-J5ecOt_Re23lEJ0sa0M-U3Q'
logging.basicConfig(level=logging.INFO) 

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
count = 3
cd = 11
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Это бот калькулятор.\nДля вызова списка команд жми /help\n")
        
@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("/sum число1 число2 - Вернет сумму двух чисел\n"
                        "/diff число1 число2 - Вернет разность двух чисел \n"
                        "/div число1 число2 - Вернет частное двух чисел \n"
                        "/mult число1 число2 - Вернет произведение двух чисел \n"
                        "/show_log показать журнал событий")
                        
@dp.message_handler(commands=['sum'])
async def calc_sum(message: types.Message):
    global count
    nums = parse_num(message.text)
    save_log(f'{get_date_time()}: {nums[0]} + {nums[1]}')
    count -= 1
    await message.reply(f'Сумма чисел {nums[0]} и {nums[1]} равна {nums[0] + nums[1]}\n')

@dp.message_handler(commands=['diff'])
async def calc_diff(message: types.Message):
    nums = parse_num(message.text)
    save_log(f'{get_date_time()}: {nums[0]} - {nums[1]}')
    await message.reply(f'Разность чисел {nums[0]} и {nums[1]} равна {nums[0] - nums[1]}\n')

@dp.message_handler(commands=['mult'])
async def calc_mult(message: types.Message):
    nums = parse_num(message.text)
    save_log(f'{get_date_time()}: {nums[0]} * {nums[1]}')
    await message.reply(f'Произведение чисел {nums[0]} и {nums[1]} равно {nums[0] * nums[1]}\n')

@dp.message_handler(commands=['div'])
async def calc_mult(message: types.Message):
    nums = parse_num(message.text)
    save_log(f'{get_date_time()}: {nums[0]} / {nums[1]}')
    await message.reply(f'Частное чисел {nums[0]} и {nums[1]} равно {nums[0] / nums[1]}.\n')

@dp.message_handler(commands=['show_log'])
async def show_log(message: types.Message):
    try:
        with open('log_bot.txt', 'r', encoding='utf-8') as log:
            log_list = log.open().splitlines()
            msg = log_list[:20]
    except:
        msg = 'Что-то пошло не так'
    await message.reply(msg)

def get_date_time():
    return str(datetime.fromtimestamp(int(time.time())))

def parse_num(msg):
    try:
        nums = msg.split(' ')
        return list(map(int, nums[1:]))
    except:
        return

def save_log(msg):
    with open('log_bot.txt', 'a', encoding='utf-8') as log:
        log.write(f'{msg}\n')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)