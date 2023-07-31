from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

colors = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Red"),
            KeyboardButton(text="Green"),
            KeyboardButton(text="Blue"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

phone = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Поширити номер телефону", request_contact=True),
            KeyboardButton("Поширити локацію", request_location=True),
        ]
    ]
)

choise = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Хочу послухати музику"),
            KeyboardButton(text="Хочу подивитись фільми/серіали"),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
)