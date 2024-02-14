from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

more_information: dict[str, str] = {
    'доп. информация': 'more_information'
}

callback_btn: dict[str, dict] = {
    'more_information': {
        'Начать работу!': 'select_type_diagram'
    },

    'select_type_diagram': {
        'Обычный': 'defalute',
        'Круглый': 'circle',
        'Стек': 'stek',
        'Точечный': 'dot',
        'Стак': 'stack'
    }
}

def generate_btn(dictionary):
    builder = InlineKeyboardBuilder()

    builder.adjust(3)

    for key, value in dictionary.items():
        builder.button(text=key, callback_data=value)

    return builder


def generate_btns(dictionary, name):
    builder = InlineKeyboardBuilder()

    builder.adjust(3)

    for key, value in dictionary[name].items():
        builder.button(text=key, callback_data=value)

    return builder
