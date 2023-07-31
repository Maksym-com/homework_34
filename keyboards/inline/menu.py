from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

first = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Button 1', callback_data='second'),
        ]
    ]
)


button_exit = InlineKeyboardButton('Exit', callback_data='exit')
button_call_manager = InlineKeyboardButton('Call manager', callback_data='call_manager')
button_test = InlineKeyboardButton('test', callback_data='test')


first.add(button_exit)
first.add(button_call_manager)

row_keyboard = InlineKeyboardMarkup().row(button_exit, button_call_manager, button_test)
button4 = InlineKeyboardButton('4', callback_data='4')
button5 = InlineKeyboardButton('5', callback_data='5')


markup3 = InlineKeyboardMarkup()

markup3.row(button_exit, button_call_manager, button_test)
markup3.add(InlineKeyboardButton('Big brother', callback_data='1'))
markup3.row(button4, button5)

social = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Youtube", url='https://www.youtube.com/'), InlineKeyboardButton("Twitch", url='https://www.twitch.com/')],
        [InlineKeyboardButton("LinkdIn", url='https://www.linkedin.com/'), ],
        [InlineKeyboardButton("Twitter", url='https://x.com/'), ],
    ]
)

music = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Daylight", url='https://open.spotify.com/track/1odExI7RdWc4BT515LTAwj',)],
        [InlineKeyboardButton("Counting stars", url='https://open.spotify.com/track/2tpWsVSb9UEmDRxAl1zhX1',)],
    ],
)

mouvies = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton("Сім душ", url='https://uakino.club/filmy/genre_drama/509-sm-dush.html'), InlineKeyboardButton("Гострі картузи (1-6 сезон)", url='https://uakino.club/seriesss/drama_series/5562-zagostren-kozirki-1-sezon.html',)],
    ],
)