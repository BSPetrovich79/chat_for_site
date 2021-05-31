# -*- coding: utf-8 -*-
from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from log_module import log
import tracemalloc
from decimal import Decimal
from config import TOKEN
import keyboards as kb
import pymysql
import config
import re

tracemalloc.start()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db_test = ''
db_prod = ''


phone_pattern = re.compile(r'^7\d{10}$')
order_id_pattern = re.compile(r'^\d+$')


def sql_query(query):
    con = pymysql.connect(host='', user='', password='', database=db_test)
    with con:
        cur = con.cursor()
        cur.execute(query)
        rows = cur.fetchone()
        print(rows)
        return rows


@dp.message_handler(commands=['start'])
async def process_command(message: types.Message):
    await message.reply("Нажмите одну из кнопок", reply_markup=kb.inline_kb_full)


@dp.callback_query_handler(lambda c: c.data == 'button10')
async def process_callback_button(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Введите номер заказа или номер телефона')


# allow_buttons = [f"button{i}" for i in range(1, 10)]
#
#
# @dp.callback_query_handler(lambda c: c.data in allow_buttons)
# async def process_callback_button(callback_query: types.CallbackQuery):
#     button_push = callback_query
#     await bot.answer_callback_query(callback_query.id, config.switch_button.get(button_push))
#     print(button_push.data)
#     push = button_push.data
#     button_request = config.switch_button.get(push)
#     print(button_request)
#     rows = sql_query(button_request)
#     await bot.send_message(callback_query.from_user.id, rows, reply_markup=kb.inline_kb_full)


@dp.message_handler(content_types=['text'])
async def get_text_messages(message):
    send = re.sub(r"\D", "", message.text)
    send = re.sub(r"^8", "7", send)
    print(len(send), send)
    if phone_pattern.match(send):
        query = config.request_db_button10["phone"].format(phone=send)
    elif order_id_pattern.match(send):
        query = config.request_db_button10["order"].format(order_id=send)
    rows = sql_query(query)
    if not rows:
        messages = 'Заказ не найден. Проверьте данные и попробуйте еще раз или переключитесь на оператора'
        await bot.send_message(message.from_user.id, messages, reply_markup=kb.inline_kb_full)
    else:
        t = rows
        print(f'Ваш заказ №{t[0]} на сумму {int(t[2])}руб. Доставка в "{t[1]}".  Статус-{t[3]}')
        answer = f'Ваш заказ №{t[0]} на сумму {int(t[2])} руб. Доставка в "{t[1]}".  Статус-{t[3]}'
        await bot.send_message(message.from_user.id, answer, reply_markup=kb.inline_kb_full)


log('END: STATUS DONE')

if __name__ == '__main__':
    executor.start_polling(dp)
