# -*- coding: utf-8 -*-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import config


inline_btn_1 = InlineKeyboardButton('Что с моим заказом', callback_data='button10')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)


inline_kb_full = InlineKeyboardMarkup(row_width=2).add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton('Связаться с оператором', url=config.url_chat))
# inline_kb_full.add(InlineKeyboardButton('Третья', callback_data='button3'))
# inline_kb_full.add(InlineKeyboardButton('Четвертая', callback_data='button4'))
# inline_kb_full.add(InlineKeyboardButton('Пятая', callback_data='button5'))
# inline_kb_full.add(InlineKeyboardButton('Шестая', callback_data='button6'))
# inline_kb_full.add(InlineKeyboardButton('Седьмая', callback_data='button7'))
# inline_kb_full.add(InlineKeyboardButton('Восьмая', callback_data='button8'))
# inline_kb_full.add(InlineKeyboardButton('Девятая', callback_data='button9'))
# inline_kb_full.add(InlineKeyboardButton('Что с моим заказом', callback_data='button10'))
# inline_kb_full.add(InlineKeyboardButton('Связаться с оператором', url=config.url_chat))
