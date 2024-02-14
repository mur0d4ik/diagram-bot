from aiogram import Router, F
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import Message
from keyboard.inline import *

router = Router()


@router.message(CommandStart())
async def CMDstart(message: Message, command: CommandObject):
    await message.answer(
        f'Привет <b>{message.from_user.username}</b>✋\nНажмите на кнопку👇',
        reply_markup=generate_btn(more_information).as_markup(resize_keyboard=True), parse_mode='HTML')


@router.message(Command('generate'))
async def CMDgenerate(message: Message, command: CommandObject):
    await message.answer(
        f'Выбирите тип диаграммы!',
        reply_markup=generate_btns(callback_btn, 'select_type_diagram').as_markup())
