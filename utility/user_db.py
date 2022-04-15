import sqlite3

con = sqlite3.connect("static/data/users.db", check_same_thread=False)
cur = con.cursor()
cur.execute(
    """
CREATE TABLE IF NOT EXISTS users (
    name TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    cart TEXT NOT NULL
)
"""
)
con.commit()


def insert_user(name, password):
    cur.execute(
        "INSERT INTO users VALUES(:name, :password, :cart)",
        {
            "name": name,
            "password": password,
            "cart": "",
        },
    )
    con.commit()


def update_cart(new_cart: list, name):
    cur.execute(
        "UPDATE users SET cart=:cart WHERE name=:name",
        {"cart": ",".join(new_cart), "name": name},
    )
    con.commit()


def add_to_cart(value: int, quantity: int, name):
    try:
        form_dct = dict(map(int, i.split()) for i in get_cart(name))
    except TypeError:
        form_dct = {}
    if value in form_dct:
        form_dct[value] += quantity
    else:
        form_dct[value] = quantity
    lst = [f"{i} {j}" for i, j in form_dct.items()]
    update_cart(lst, name)


def get_cart(name):
    try:
        temp = (
            cur.execute("SELECT cart FROM users WHERE name = :name", {"name": name})
            .fetchall()[0][0]
            .split(",")
        )
        return [i for i in temp if i]
    except IndexError:
        return []


def get_processed_cart(name):
    temp = get_cart(name)
    final_cart = []
    for i in temp:
        pid, quantity = map(int, i.split())
        final_cart.append((pid, quantity))
    return final_cart


def verify_password(name, password):
    try:
        temp = cur.execute(
            "SELECT password FROM users WHERE name = :name", {"name": name}
        ).fetchall()[0][0]
    except IndexError:
        return False
    return password == temp


def reset_cart(new_cart: list, name):
    cur.execute(
        "UPDATE users SET cart='' WHERE name=:name",
        {name: "name"},
    )
    con.commit()


def remove_from_cart(value: int, name):
    try:
        form_dct = dict(map(int, i.split()) for i in get_cart(name))
    except TypeError:
        form_dct = {}
    if value in form_dct:
        del form_dct[value]
    lst = [f"{i} {j}" for i, j in form_dct.items()]
    update_cart(lst, name)


def modify_cart(value: int, quantity: int, name):
    try:
        form_dct = dict(map(int, i.split()) for i in get_cart(name))
    except TypeError:
        form_dct = {}
    if value in form_dct:
        form_dct[value] = quantity
    lst = [f"{i} {j}" for i, j in form_dct.items()]
    update_cart(lst, name)


def check_username_exists(name):
    return bool(
        cur.execute(
            "select name from users where name=:name", {"name": name}
        ).fetchall()
    )
