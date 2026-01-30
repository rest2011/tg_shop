from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

inline_kb = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text='Кнопка 1', callback_data='Btn_1'),
    InlineKeyboardButton(text='URL', url='ya.ru'),
    InlineKeyboardButton(text='Кнопка 2', callback_data='Btn_2')
]
])

reply_kb = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text='Кнопка 3'),
    KeyboardButton(text='Кнопка 4')
]
])

reply_kb2 = ReplyKeyboardBuilder()
reply_kb2.button(text='Кнопка 5')
reply_kb2.button(text='Кнопка 6')
reply_kb2.adjust(1)

inline_kb2 = InlineKeyboardBuilder()
inline_kb2.button(text='Кнопка 7', callback_data='btn_7')
inline_kb2.button(text='Кнопка 8', callback_data='btn_8')
inline_kb2.button(text='URL', url='ya.ru')

start_kb2 = InlineKeyboardBuilder()
start_kb2.button(text='Кошки', callback_data='Cats')
start_kb2.button(text='Собаки', callback_data='Dogs')
start_kb2.adjust(2)