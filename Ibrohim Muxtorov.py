import psycopg2

conn = psycopg2.connect(
    dbname="n47",
    password="123",
    host="locolhost",
    port="5432"
)

cur = conn.cursor()

create_table_query = '''
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price NUMERIC(10, 2),
    color VARCHAR(50),
    image VARCHAR(255)
)
'''

insert_into = '''
INSERT INTO products(id, name, price, color, image) VALUES(%s, %s, %s, %s, %s)
'''

cur.execute(create_table_query)

conn.commit()

cur.close()
conn.close()

#2 - misol
import sqlite3

conn = sqlite3.connect('products.db')
cursor = conn.cursor()


def create_product_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id PRIMARY KEY,
                        name TEXT NOT NULL,
                        price REAL NOT NULL,
                        quantity INTEGER NOT NULL)''')
    conn.commit()


def insert_product(name, price, quantity):
    cursor.execute('''INSERT INTO products (name, price, quantity) VALUES (%, %, %)''')
    conn.commit()


def select_all_products():
    cursor.execute('''SELECT * FROM products''')
    products = cursor.fetchall()
    return products


def update_product(id, name, price, quantity):
    cursor.execute('''UPDATE products SET name=?, price=?, quantity=? WHERE id=?''')
    conn.commit()


def delete_product(id):
    cursor.execute('''DELETE FROM products WHERE id=?''')
    conn.commit()


def close_connection():
    conn.close()


create_product_table()


#3 - Misol


class Alphabet:
    def __iter__(self):
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.letters):
            letter = self.letters[self.index]
            self.index += 1
            return letter
        else:
            raise StopIteration


alph = Alphabet()
for letter in alph:
    print(letter)

# 4 -misol

import threading
import time


def print_numbers(start, end):
    for num in range(start, end + 1):
        print(num)


def print_letters():
    letters = 'ABCDE'
    for letter in letters:
        print(letter)
        time.sleep(1)


if __name__ == "__main__":
    start_num = 1
    end_num = 5

    num_thread = threading.Thread(target=print_numbers, args=(start_num, end_num))

    letter_thread = threading.Thread(target=print_letters)

    num_thread.start()
    letter_thread.start()

    num_thread.join()
    letter_thread.join()

    print("LOOP STOP")


# 5 - misol

class Product:
    def __init__(self, name, price, color, image):
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self):
        conn = psycopg2.connect(
            dbname="Ibrohim",
            password="123",
            host="localhost",
            port="5432"
        )

        cur = conn.cursor()

        insert_into = '''
        INSERT INTO products(name, price, color, image) VALUES(%s, %s, %s, %s) RETURNING id
        '''

        cur.execute(insert_into, (self.name, self.price, self.color, self.image))
        inserted_id = cur.fetchone()[0]

        conn.commit()

        cur.close()
        conn.close()

        return inserted_id


product = Product("Chair", 50.00, "Brown", "chair.jpg")
inserted_id = product.save()
print("", inserted_id)





#6 -misol

class DbConnect:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

    def __enter__(self):
        self.conn = psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )
        self.cur = self.conn.cursor()
        return self.conn, self.cur

    def __exit__(self, exc_type, exc_value, traceback):
        self.cur.close()
        self.conn.close()

with DbConnect('dbname', 'user', 'password', 'host', 'port') as (conn, cur):
    cur.execute("SELECT * FROM table_name")
    rows = cur.fetchall()
    for row in rows:

        print(row)



#7- misol

import requests
import psycopg2

url = f'https://dummyjson.com/products/'

r = requests.get(url)

conn = psycopg2.connect(dbname='n47',
                        user='postgres',
                        password='123',
                        host='localhost',
                        port=5432)

create_table_products_query = """create table if not exists products(
        id serial primary key,
        title varchar(255),
        description text,
        price int,
        discountPercentage float,
        rating float,
        stock int,
        brand varchar(255),
        category varchar(200),
        thumbnail varchar(255),
        images jsonb
);"""

cur = conn.cursor()

try:
    cur.execute(create_table_products_query)
    conn.commit()
except Exception as e:
    print("Error creating table:", e)

insert_into_query = """insert into products (title, description, price, discountPercentage, rating, stock, brand, category, thumbnail, images)
    values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
"""

for product in r.json()['products']:
    try:
        cur.execute(insert_into_query, (
            product['title'], product['description'], product['price'], product['discountPercentage'], product['rating'],
            product['stock'], product['brand'], product['category'], product['thumbnail'], str(product['images'])))
        conn.commit()
    except Exception as e:
        print("Xatolik!!!", e)

cur.close()
conn.close()
