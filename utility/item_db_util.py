import sqlite3
from random import shuffle
from utility import user_db
from difflib import SequenceMatcher

con = sqlite3.connect("static/data/items.db", check_same_thread=False)
cur = con.cursor()
# Initialize database if it doesn't exist
cur.execute(
    """
CREATE TABLE IF NOT EXISTS items (
    id INTEGER(8) PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER(8),
    image TEXT DEFAULT 'items/default.png'
)
"""
)
con.commit()


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def get_items(query=""):
    lst = cur.execute("SELECT * FROM items").fetchall()
    if query:
        lst.sort(key=lambda i: similar(i[1], query), reverse=True)
    else:
        shuffle(lst)
    return lst


def get_item_details(product_id):
    return cur.execute(
        "SELECT * FROM items WHERE id = :product_id", {
            "product_id": product_id}
    ).fetchall()[0]


def connect_cart_item(name):
    try:
        form_dct = dict(map(int, i.split()) for i in user_db.get_cart(name))
    except TypeError:
        form_dct = {}
    return [get_item_details(i) + tuple([form_dct[i]]) for i in form_dct]


def calculate_prices(name):
    try:
        form_dct = dict(map(int, i.split()) for i in user_db.get_cart(name))
    except TypeError:
        form_dct = {}
    prices = []
    for i in form_dct:
        _, _, price, _ = get_item_details(i)
        quantity = form_dct[i]
        prices.append(price * quantity)
    return prices
