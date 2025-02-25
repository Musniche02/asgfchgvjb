from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Sherik kerak"), KeyboardButton(text="Ish joyi kerak")],
        [KeyboardButton(text="Hodim kerak"), KeyboardButton(text="Ustoz kerak")],
        [KeyboardButton(text="Shogird kerak")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Buttonlardan birini tanlang",
    one_time_keyboard=True
)