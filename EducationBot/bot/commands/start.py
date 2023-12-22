from aiogram.types import Message
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup

from aiogram.utils.keyboard import (ReplyKeyboardMarkup,
                                    ReplyKeyboardBuilder,
                                    InlineKeyboardMarkup,
                                    InlineKeyboardBuilder,
                                    KeyboardButton,
                                    KeyboardButtonPollType)


async def start(message: Message):
    menu_builder = ReplyKeyboardBuilder()
    menu_builder.button(
        text='Помощь'
    )
    menu_builder.add(
        KeyboardButton(text='Отправить контакт', request_contact=True),
    )
    menu_builder.row(
        KeyboardButton(text='Отправить голосование', request_poll=KeyboardButtonPollType(type='quiz'))
    )

    await message.answer(
        'Меню',
        reply_markup=menu_builder.as_markup(resize_keyboard=True)
        # reply_markup=ReplyKeyboardMarkup(keyboard=menu_builder.export())
    )
