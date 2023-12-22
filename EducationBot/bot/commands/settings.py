from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from bot.commands.callback_data_states import TestCallbackData


async def settings_command(message: Message):
    settings_markup = InlineKeyboardBuilder()
    settings_markup.button(
        text='Яндекс',
        url='yandex.ru'
    )
    settings_markup.button(
        text='Помощь',
        callback_data=TestCallbackData(text='Привет', user_id=message.from_user.id)
    )
    await message.answer('Настройки', reply_markup=settings_markup.as_markup())


async def settings_callback(call: CallbackQuery, callback_data: TestCallbackData):
    await call.message.answer(callback_data.text + ',' + str(callback_data.user_id))
