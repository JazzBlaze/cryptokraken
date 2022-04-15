if __name__ == "__main__":
    import sqlite3

    con = sqlite3.connect("static/data/items.db")
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
    temp = con.execute("SELECT id FROM items ORDER BY id DESC LIMIT 1").fetchall()
    curr_id = temp[0][0] if temp else 0
    for _ in range(int(input("Enter number of items to include in DB: "))):
        curr_id += 1
        name = input("Enter name of product: ")
        price = int(input("Enter price of product in Rs: "))
        image = input("Enter path to image: ") or "items/default.png"
        cur.execute(
            "INSERT INTO items VALUES(:curr_id, :name, :price, :image)",
            {
                "curr_id": curr_id,
                "name": name,
                "price": price,
                "image": image,
            },
        )
    con.commit()
