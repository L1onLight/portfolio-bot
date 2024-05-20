from aiogram import types
import buttons

HELLO = types.InlineKeyboardMarkup(
    inline_keyboard=buttons.HELLO
)

BACK = types.InlineKeyboardMarkup(
    inline_keyboard=[buttons.BACK]
)

RESUME = types.InlineKeyboardMarkup(
    inline_keyboard=[buttons.CV, buttons.BACK]
)

REPOSITORIES = types.InlineKeyboardMarkup(inline_keyboard=buttons.REPOSITORIES)
REPOSITORY = types.InlineKeyboardMarkup(inline_keyboard=[buttons.PROJECTS + buttons.BACK])
