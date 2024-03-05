import io

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.methods import GetChatMember
from aiogram.types import Message, CallbackQuery
from aiogram.types.input_file import BufferedInputFile
from aiogram.methods.get_chat_member import *
from diagrams.function_diagrams import *
from handlers.utils import *
from keyboard.inline import *
from state.state import *

router = Router()


@router.callback_query()
async def anycallback(call: CallbackQuery, state: FSMContext):
    await call.message.delete()

    global select_type_diagramm
    select_type_diagramm = call.data

    if call.data not in callback_btn['select_type_diagram'].values():
        await call.message.answer_photo(
            photo=text[call.data][-1],
            caption=text[call.data][0],
            reply_markup=generate_btns(callback_btn, call.data).as_markup())

    else:
        await call.message.answer_photo(
            photo=text[select_type_diagramm][-1],
            caption=text[select_type_diagramm][0],
            parse_mode='HTML')
        await state.set_state(Info_in_generate_diagram.info)


@router.message(Info_in_generate_diagram.info)
async def stateInfo_in_generate_diagram(message: Message, state: FSMContext):
    list_convert = await string_to_list(select_type_diagramm, message.text)

    img = await generate_diagrams(select_type_diagramm, list_convert[0], list_convert[-1])

    try:
        await message.answer_photo(
            photo=BufferedInputFile(file=img, filename='diagram'),
            caption='Результат!',
            reply_markup=generate_btn(try_generate).as_markup())

    except:
        await message.answer('Ой что-то пошло не так!',
            reply_markup=generate_btn(try_generate).as_markup())

    await state.clear()


@router.message()
async def givephoto(message: Message):
    if message.photo:
        await message.answer(message.photo[-1].file_id)

    else:
        user_status = GetChatMember(chat_id=-1002108950585, user_id=message.from_user.id)   #Ошибка
        print(user_status)
        if user_status != None:
            await message.answer(
                'Если нужно сгенерировать диаграмму то введите команду <code>/generate</code>',
                parse_mode='HTML')

        else:
            await message.answer('Подпишитесь на канал @rindoblo!')