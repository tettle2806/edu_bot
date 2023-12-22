from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandObject
from bot.commands.bot_commands import bot_commands
from aiogram.utils.keyboard import InlineKeyboardButton

async def help_command(message: Message, command: CommandObject):
    if command.args:
        for cmd in bot_commands:
            if cmd[0] == command.args:
                return await message.answer(
                    f"{cmd[0]} - {cmd[1]}\n\n{cmd[2]}"
                )
        else:
            return await message.answer('Команда не найдена')
    return help_func(message)


async def help_func(message: Message):
    return await message.answer(
        'Помощь и справка о боте\n'
        'Для того что-бы получить информацию о команде используй /help <команда>\n'
    )


async def call_help_func(call: CallbackQuery):
    return await call.message.edit_text(
        'Помощь и справка о боте\n'
        'Для того что-бы получить информацию о команде используй /help <команда>\n',
        reply_markup=call.message.reply_markup
    )


async def clear_call_help_func(call: CallbackQuery):
    await call.message.edit_text(
        'Очищено'
    )
