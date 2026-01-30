import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

import keyboards.keyboard as kb
import photo.photo as ph

TOKEN = '8493031792:AAGBtQCJWl9JcnA-aaEcA2Nb-H8ZgK2nASA'
dp = Dispatcher()
bot = Bot(token=TOKEN)

# @dp.message(CommandStart())
# async def start(message: Message):
#     await message.answer(f"Привет, {message.from_user.full_name}"
#                          f"\n\nИспользуй команду /help",
#                          reply_markup=kb.reply_kb2.as_markup(resize_keyboard=True)
#                          )

@dp.message(CommandStart())
async def start(message: Message, bot: Bot):
    photo = ph.phot_start
    await bot.send_photo(photo=photo, 
                         caption=f'Привет, {message.from_user.full_name}'
                         f'\n<b>Жирный</b>',
                        parse_mode='HTML',
                         chat_id=message.from_user.id,
                         reply_markup=kb.start_kb2.as_markup()
                         )
    
@dp.callback_query(F.data == 'Cats')    
async def cats(call: CallbackQuery):
    phot = ph.url_cat
    await call.bot.send_photo(photo=phot, 
                              caption='Котик'
                              '*ЖИРНЫЙ*'
                              '_КУРСИВ_', 
                              parse_mode='Markdown',
                              chat_id=call.from_user.id)
    
@dp.message(F.text == 'Cats')    
async def cats(message: Message):
    phot = ph.url_cat
    await bot.send_photo(photo=phot, 
                              caption='Котик'
                              '*ЖИРНЫЙ*'
                              '_КУРСИВ_', 
                              parse_mode='Markdown',
                              chat_id=message.from_user.id)    

@dp.callback_query(F.data == 'Dogs')    
async def cats(call: CallbackQuery):
    phot = ph.url_cat
    await call.bot.send_photo(photo=phot, caption='Щенок', chat_id=call.from_user.id)    

@dp.message(F.text.lower().contains('привет'))
async def check_filter(message: Message):
    await message.answer('Это магический фильтр')

@dp.callback_query(F.data == 'btn_7')
async def callback(call: CallbackQuery):
    await call.message.edit_text('Кнопка нажата')    

# @dp.callback_query()
# async def check_callback(call: CallbackQuery):
#     if call.data == 'btn_7':
#         await call.message.answer("Вы нажали кнопку")
#     elif call.data == 'btn_8':
#         await call.message.answer("Вы нажали другую кнопку")

@dp.message(Command('help'))
async def help(message: Message):
    await message.answer('Вы запросили помощь')   

@dp.message(F.photo)    
async def photo_id(message: Message):
    photo_id = message.photo[-1].file_id
    await message.answer(photo_id)

@dp.message()
async def echo(mes: Message):
    await mes.reply(mes.text)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
