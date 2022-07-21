import sqlite3
import asyncio
import random
import os
import config
from random import choice
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from aiogram.dispatcher.webhook import SendMessage
from aiogram.types import ChatActions
from aiogram.utils.executor import start_webhook
from config import TOKEN
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton 

bot = Bot(token=TOKEN)

conn = sqlite3.connect('db/fics_database.db', check_same_thread=False)
cursor = conn.cursor()

def db_table_val(user_id: int, user_name: str, user_surname: str, username: str):
	cursor.execute('INSERT INTO users (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
	conn.commit()
#eng
button_hi1 = KeyboardButton('Main menu')#button_hi

button_buy1 = KeyboardButton('Go to tarif view')#button_buy

button_purshace5 = KeyboardButton('Buying hentai games forever')#button_purshace
button_purshace6 = KeyboardButton('Buying hentai games for a month')#button_purshace0
button_purshace7 = KeyboardButton('Buy loli private forever')#button_purshace3
button_purshace8 = KeyboardButton('Buying loli private for a month')#button_purshace4
button_purshace9 = KeyboardButton('Loli private')#button_purshace1
button_purshace10 = KeyboardButton('Hentai games')#button_purshace2
button_leave3 = KeyboardButton('Main menu')#button_leave
button_leave4 = KeyboardButton('Back️')#button_leave1
button_leave5 = KeyboardButton('Back')#button_leave2
button_tarif5 = KeyboardButton('Forever️')#tarif1
button_tarif6 = KeyboardButton('For a mounth️')#tarif2
button_tarif7 = KeyboardButton('Forever')#tarif3
button_tarif8 = KeyboardButton('For a mounth')#tarif4
button_off1 = KeyboardButton('Return buttons')#button_off

greet_kb11 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi1)#greet_kb1
greet_kb12 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_purshace9, button_purshace10, button_leave3)#greet_kb2
greet_kb13 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_tarif5, button_tarif6, button_leave3)#greet_kb3
greet_kb14 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_purshace5, button_leave4, button_leave3)#greet_kb4
greet_kb15 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_purshace6, button_leave4, button_leave3)#greet_kb5
greet_kb16 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_tarif7, button_tarif8, button_leave3) #greet_kb6
greet_kb17 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_purshace7, button_leave5, button_leave3) #навсегда #greet_kb7
greet_kb18 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_purshace8, button_leave5, button_leave3) #на месяц #greet_kb8
greet_kb19 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_purshace8, button_leave5, button_leave3)#просмотр тарифа #greet_kb9
greet_kb20 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_leave3)#greet_kb10

button9 = KeyboardButton('Tarif')#button1
button10 = KeyboardButton('Reviews')#button2
button11 = KeyboardButton('Purshace')#button3

markup6 = ReplyKeyboardMarkup().add( #markup3
    button9).add(button10).add(button11)

markup7 = ReplyKeyboardMarkup().row( #markup4
    button9, button10, button11
)

markup8 = ReplyKeyboardMarkup().row( #start #markup5
    button9, button10, button11
).add(KeyboardButton('Admins'))

button12 = KeyboardButton('Channel')#button4
button13 = KeyboardButton('Chat')#button5
button14 = KeyboardButton('Help')#button6
markup8.row(button12, button13).add(KeyboardButton('Set language'))
markup8.insert(button14).add(KeyboardButton('Support the channel'))


button15 = KeyboardButton('Loli private')
button16 = KeyboardButton('Hentai games')

markup9 = ReplyKeyboardMarkup().row(
    button15, button16
)

markup7 = ReplyKeyboardMarkup().row(
    button15, button16).add(KeyboardButton('Admins'))
#ru
button_hi = KeyboardButton('Главное меню')

button_buy = KeyboardButton('Перейти к просмотру тарифа')

button_purshace = KeyboardButton('Покупка хентай игр навсегда')
button_purshace0 = KeyboardButton('Покупка хентай игр на месяц')
button_purshace3 = KeyboardButton('Покупка лоли привата навсегда')
button_purshace4 = KeyboardButton('Покупка лоли привата на месяц')
button_purshace1 = KeyboardButton('Лоли приват')
button_purshace2 = KeyboardButton('Хентай игры')
button_leave = KeyboardButton('Главное меню')
button_leave1 = KeyboardButton('Назад️')
button_leave2 = KeyboardButton('Назад')
button_tarif1 = KeyboardButton('Навсегда️')#tarif1 = tarif5
button_tarif2 = KeyboardButton('На месяц️')#tarif2 = tarif6
button_tarif3 = KeyboardButton('Навсегда')
button_tarif4 = KeyboardButton('На месяц')
button_off = KeyboardButton('Вернуть кнопки')
button_russian = KeyboardButton('Русский')
button_english = KeyboardButton('English')
button_panel = KeyboardButton('Админ-панель')
button_admin = KeyboardButton('Рассылка')
button_mnelen = KeyboardButton('Тык')
button_post = KeyboardButton('Пост')


greet_kb = ReplyKeyboardMarkup()
greet_kb.add(button_hi)
greet_kb1 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_hi)
greet_kb2 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_purshace1, button_purshace2, button_leave)
greet_kb3 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_tarif1, button_tarif2, button_leave)
greet_kb4 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_purshace, button_leave1, button_leave)
greet_kb5 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_purshace0, button_leave1, button_leave)
greet_kb6 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_tarif3, button_tarif4, button_leave) 
greet_kb7 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_purshace3, button_leave2, button_leave) #навсегда
greet_kb8 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_purshace4, button_leave2, button_leave) #на месяц
greet_kb9 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_purshace4, button_leave2, button_leave) #просмотр тарифа
greet_kb10 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_leave)
greet_kb0 = ReplyKeyboardMarkup(resize_keyboard=True).add(button_russian, button_english)

greet_kb_panel = ReplyKeyboardMarkup(resize_keyboard=True).add(button_panel, button_leave)
greet_kb_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_admin, button_mnelen, button_leave, button_post)


button1 = KeyboardButton('Тариф')
button2 = KeyboardButton('Отзывы')
button3 = KeyboardButton('Покупка')

markup3 = ReplyKeyboardMarkup().add(
    button1).add(button2).add(button3)

markup4 = ReplyKeyboardMarkup().row(
    button1, button2, button3
)

markup5 = ReplyKeyboardMarkup().row(
    button1, button2, button3
).add(KeyboardButton('Админы'))

button4 = KeyboardButton('Канал')
button5 = KeyboardButton('Чат')
button6 = KeyboardButton('Помощь')
button_admin1 = KeyboardButton('>>')
markup5.row(button4, button5, button_admin1).add(KeyboardButton('Сменить язык'))
markup5.insert(button6).add(KeyboardButton('Поддержать канал'))

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await bot.send_chat_action(message.chat.id, ChatActions.TYPING)
    await asyncio.sleep(3)
    await message.reply("Выбери свой язык", reply_markup=greet_kb0)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username
    db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

@dp.message_handler(commands=['photo'])
async def process_start_command(message: types.Message):
    photo = open('C:/Users/ок/AppData/Local/Programs/Python/Python38/MY PROJECT BOT/photos/photo_2022-04-25_13-11-27.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo, "Отправляю вам узбекского кота")
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await asyncio.sleep(10)
    await bot.send_message(message.from_user.id, "Сообщение отрпавилось ровно через 10 секунд")
  
@dp.message_handler(text=['Главное меню'])
async def process_start_command(message: types.Message):
    await message.reply("Жми на кнопки ниже", reply_markup=markup5)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Сменить язык'])
async def process_start_command(message: types.Message):
    await message.reply("Выбери свой язык\nSet your language", reply_markup=greet_kb0)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

admin_id = 1451152953, 1753180282
owner_id = 1451152953

@dp.message_handler(user_id=admin_id, text=['Тык'])
async def process_start_command(message: types.Message):
    photo = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo1 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo2 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo3 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo4 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo5 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo6 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo7 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo8 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo9 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo10 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo11 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo12 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo13 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo14 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo15 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo16 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo17 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo18 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo19 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo20 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo21 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo22 = open('loli/' + random.choice(os.listdir('loli')), 'rb')
    photo23 = open('loli/' + random.choice(os.listdir('loli')), 'rb')    
    await bot.send_photo(-1001633496227, photo, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo1, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo2, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo3, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo4, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo5, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo6, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo7, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo8, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo9, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo10, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo11, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo12, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo13, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo14, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo15, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo16, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo17, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo18, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo19, caption='#loli')
    await asyncio.sleep(40)
    await bot.send_photo(-1001633496227, photo20, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo21, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo22, caption='#loli')
    await asyncio.sleep(1)
    await bot.send_photo(-1001633496227, photo23, caption='#loli')
    await asyncio.sleep(1)

@dp.message_handler(user_id=admin_id, text=['Админ-панель'])
async def process_admin(message: types.Message):
    await message.reply("Добро пожаловать в админ меню!\nЗдесь ты можешь запустить рассылку и многое другое...", reply_markup=greet_kb_admin)
@dp.message_handler(text=['Админ-панель'])
async def process_admin(message: types.Message):
    await message.reply("У вас нет доступа к этому меню:(", reply_markup=greet_kb10)
    
@dp.message_handler(user_id=admin_id, text=['Пост'])
async def process1(message: types.Message):
    await message.reply("Данич, сендай коммандой /send + photo, иначе полная ебень будет")

@dp.message_handler(content_types=["photo"], text=['/send'], user_id=admin_id)
async def replying(pic):
    buttons = [
        types.InlineKeyboardButton(text="Купить", url="https://t.me/zxc_curs3d"),
        types.InlineKeyboardButton(text="Предосмотр приваточки", url="https://t.me/+L9T8nojQVAc0ZDQy"),
        ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await bot.send_photo(-1001566342643, pic.photo[-1].file_id, caption=f'#арт\n\nКупить нашу приваточку вы можете тут', reply_markup=keyboard)
    
@dp.message_handler(content_types=["photo"])
async def replying(pic):
    await bot.send_photo(-1001736753651, pic.photo[-1].file_id, caption=f'Пользователь @{pic.from_user.username} c ником: {pic.from_user.first_name}\nOтправил картинку c описанием: {pic.caption}')
    photo = open('C:/Users/ок/AppData/Local/Programs/Python/Python38/MY PROJECT BOT/photos/sticker.webp', 'rb')
    await bot.send_photo(pic.from_user.id, photo, caption='Я ещё не научился отвечать на фотографии(')
  
@dp.message_handler(text=['>>'])
async def process_admin(message: types.Message):
    await message.reply("Скрытое меню", reply_markup=greet_kb_panel)

@dp.message_handler(text=['Русский'])
async def process1(message: types.Message):
    await message.reply("Жми на кнопки ниже", reply_markup=markup5)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username
    db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

@dp.message_handler(text=['Вернуть кнопки'])
async def process_start_command(message: types.Message):
    await message.reply("Жми на кнопки ниже", reply_markup=markup5)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    
@dp.message_handler(text=['Тариф'])
async def process_start_command(message: types.Message):
    await message.reply("Выбери то, что тебе нужно", reply_markup=greet_kb2)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Хентай игры'])
async def process_start_command(message: types.Message):
    await message.reply("Выбери из этого меню", reply_markup=greet_kb3)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Лоли приват'])
async def process_start_command(message: types.Message):
    await message.reply("Выбери из этого меню", reply_markup=greet_kb6)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Назад'])
async def process_start_command(message: types.Message):
    await message.reply("Выбери из этого меню", reply_markup=greet_kb6)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Навсегда️'])
async def process_start_command(message: types.Message):
    await message.reply("Цена: 399 рублей\nВыберите то, что тебе нужно", reply_markup=greet_kb4)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    
@dp.message_handler(text=['На месяц️'])
async def process_start_command1(message: types.Message):
    await message.reply("Цена: 99 рублей\nВыберите то, что тебе нужно", reply_markup=greet_kb5)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Навсегда'])
async def process_start_command(message: types.Message):
    await message.reply("Цена: 499 рублей\nВыберите то, что тебе нужно", reply_markup=greet_kb7)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    
@dp.message_handler(text=['На месяц'])
async def process_start_command1(message: types.Message):
    await message.reply("Цена: 199 рублей\nВыберите то, что тебе нужно", reply_markup=greet_kb8)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Назад️'])
async def process_start_command(message: types.Message):
    await message.reply("Выбери из этого меню", reply_markup=greet_kb3)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Канал'])
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Канал", url="https://t.me/+POUXwtQtmqUxNGJi"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Ссылка на наш канал", reply_markup=keyboard)
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Чат'])
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Чатик", url="https://t.me/+ykdDfqCpnj4yMGUy"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Ссылка на наш чатик", reply_markup=keyboard)
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Отзывы'])
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Отзывы после покупок привата", url="https://t.me/+uboiWSK-HXQ1NTRi"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Ссылка на наш чатик", reply_markup=keyboard)
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Поддержать канал'])
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Поддержать нас донатиком ☺️ ", url="https://www.donationalerts.com/r/kijio"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Поддержать наш канал", reply_markup=keyboard)
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Главное меню'])
async def process_start_command(message: types.Message):
    await message.reply("Жми на кнопки ниже", reply_markup=markup5)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Админы'])
async def process_start_command(message: types.Message):
    await message.reply("Владелец: @zxc_curs3d\nКодер, написавший этого бота: @zxc_curs3d\nГл. Админ: @kijio07", reply_markup=greet_kb1)
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    
@dp.message_handler(text=['Покупка'])
async def process_hi4_command(message: types.Message):
    await message.reply("Модуль в разработке", reply_markup=greet_kb1)
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(commands=['start', 'help'])
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Пропиши комманду /start ")
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}') 

@dp.message_handler(text=['Помощь'])
async def process_help_command(message: types.Message):
    await message.reply("Что тебя интересует? Тыкай на кнопки ниже\nПо всем вопросам: @zxc_curs3d ")
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}') 

#eng
@dp.message_handler(text=['English'])
async def process_start_command(message: types.Message):
    await message.reply("Click the buttons below", reply_markup=markup8)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username
    db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username)

@dp.message_handler(text=['Set language'])
async def process_start_command(message: types.Message):
    await message.reply("Выбери свой язык\nSet your language", reply_markup=greet_kb0)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

dp.message_handler(text=['Return buttons'])
async def process_start_command(message: types.Message):
    await message.reply("Click the buttons below", reply_markup=markup8)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Tarif'])
async def process_start_command(message: types.Message):
    await message.reply("Choose what you need", reply_markup=greet_kb12)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Hentai games'])
async def process_start_command(message: types.Message):
    await message.reply("Choose from this menu", reply_markup=greet_kb13)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Loli private'])
async def process_start_command(message: types.Message):
    await message.reply("Choose from this menu", reply_markup=greet_kb16)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Back'])
async def process_start_command(message: types.Message):
    await message.reply("Choose from this menu", reply_markup=greet_kb16)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Forever️'])
async def process_start_command(message: types.Message):
    await message.reply("Price: 399 rubles\nChoose what you need", reply_markup=greet_kb14)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    
@dp.message_handler(text=['For a mounth️'])
async def process_start_command1(message: types.Message):
    await message.reply("Price: 99 rubles\nChoose what you need", reply_markup=greet_kb15)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Forever'])
async def process_start_command(message: types.Message):
    await message.reply("Price: 499 rubles\nChoose what you need", reply_markup=greet_kb17)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    
@dp.message_handler(text=['For a mounth'])
async def process_start_command1(message: types.Message):
    await message.reply("Price: 199 rubles\nChoose what you need", reply_markup=greet_kb18)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Back️'])
async def process_start_command(message: types.Message):
    await message.reply("Choose from this menu", reply_markup=greet_kb13)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Channel'])
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Channel", url="https://t.me/+POUXwtQtmqUxNGJi"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Link to our channel", reply_markup=keyboard)
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Chat'])
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Chat", url="https://t.me/+ykdDfqCpnj4yMGUy"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Link to our chatl", reply_markup=keyboard)
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Reviews'])
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Reviews after purchases privat", url="https://t.me/+uboiWSK-HXQ1NTRi"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Reviews after purchases privat", reply_markup=keyboard)
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Support the channel'])
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="Support us with a donation ☺️", url="https://www.donationalerts.com/r/kijio"),
    ]
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(*buttons)
    await message.answer("Support our channel", reply_markup=keyboard)
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Main menu'])
async def process_start_command(message: types.Message):
    await message.reply("Click the buttons bellow", reply_markup=markup8)
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(text=['Admins'])
async def process_start_command(message: types.Message):
    await message.reply("Owner: @zxc_curs3d\nCoder who wrote this bot: @zxc_curs3d\nMain admin: @kijio07", reply_markup=greet_kb20)
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    
@dp.message_handler(text=['Purshace'])
async def process_hi4_command(message: types.Message):
    await message.reply("Module under developmen", reply_markup=greet_kb20)
    await bot.send_message(-1001689688175, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

@dp.message_handler(commands=['start', 'help'])
@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Write a command /start ")
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}') 

@dp.message_handler(text=['Help'])
async def process_help_command(message: types.Message):
    await message.reply("What are you interested in? Click on the buttons below\nFor all questions: @zxc_curs3d ")
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}') 

@dp.message_handler(user_id=owner_id, text=['Рассылка'])
async def process_admin(message: types.Message):
    await message.reply(f'Введите текст рассылки')
@dp.message_handler(user_id=owner_id)
async def process_admin(message: types.Message):
        con = sqlite3.connect("db/fics_database.db")
        cur = con.cursor()
        rows = cur.execute('SELECT `user_id` FROM `users`').fetchall()
        for row in rows:
                await bot.send_message(row[0], f'{message.text}')
@dp.message_handler(user_id=admin_id, text=['Рассылка'])
async def process_admin(message: types.Message):
    await message.reply(f'Недостаточно прав, вы можете заливать контент в приват или канал')
@dp.message_handler(text=['Рассылка'])
async def process_admin(message: types.Message):
    await message.reply(f'Недостаточно прав')
       
@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.from_user.id, "Русский: Напиши комманду /start\nПотому что я тебя не понимаю😢\nEnglish: Write a command /start\nBecause I don't understand you 😢")
    await bot.send_message(1451152953, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')
    await bot.send_message(-1001674185918, f'Пользователь @{message.from_user.username} c ником: {message.from_user.first_name} написал в бота это: {message.text}')

if __name__ == '__main__':
    executor.start_polling(dp)

