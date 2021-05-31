# -*- coding: utf-8 -*-
TOKEN = ''

url_chat = 'https://t.me/.....'

request_db_button10 = {
    "order": 'SELECT order_id, shipping_address_1, total, s.name as \'Статус\' FROM `order` o inner '\
             'join order_status s on s.order_status_id=o.order_status_id WHERE o.order_id={order_id}',

    "phone": 'SELECT order_id, shipping_address_1, total, s.name as \'Статус\' FROM `order` o inner '\
             'join order_status s on s.order_status_id=o.order_status_id WHERE o.telephone={phone}',
}


# switch_button = {'button1': "SELECT * FROM product",
#                  'button2': "SELECT * FROM product",
#                  'button3': "SELECT * FROM product",
#                  'button4': "SELECT * FROM product",
#                  'button5': "SELECT * FROM product",
#                  'button6': "SELECT * FROM product",
#                  'button7': "SELECT * FROM product",
#                  'button8': "SELECT * FROM product",
#                  'button9': "SELECT * FROM product"}

