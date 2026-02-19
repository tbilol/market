from psycopg2 import connect
import json

conn = connect(
    host="127.0.0.1",
    user="postgres",
    password="1",
    database="market",
    port="5432"
)

cur = conn.cursor()

# PRODUCT METHODS
def get_products():
    cur.execute("SELECT * FROM product")
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    result = [dict(zip(columns, row)) for row in rows]
    data = [json.dumps(result, indent=4)]
    r = json.loads(data[0])
    return r

def post_product(name: str, price: int, unit:str, category_name: str):
    cur.execute("insert into product (name, price, unit, category_name) values (%s, %s, %s, %s)", (name, price, unit, category_name))
    conn.commit()
    return {"message": "Product successfully added"}


def update_product(product_id: int, name: str, price: int, unit:str, category: str):
    cur.execute("update product set name=%s, price=%s, unit=%s, category_name=%s where id=%s", (name, price, unit, category,product_id))
    conn.commit()
    return {"message": "Product successfully updated"}


def delete_product(product_id: str):
    cur.execute("delete from product where id=%s",(product_id,))
    conn.commit()
    return {"message": "Product successfully deleted"}


# CATEGORY METHODS
def get_category():       # GET
    cur.execute("SELECT * FROM category")
    rows = cur.fetchall()
    columns = [desc[0] for desc in cur.description]
    result = [dict(zip(columns, row)) for row in rows]
    json_data = json.dumps(result, indent=4)
    return json.loads(json_data)

def post_category(name: str):  # POST
    cur.execute("INSERT INTO category (name) VALUES (%s);", (name,))
    conn.commit()
    return {"message": "Category successfully added"}

def delete_category(category_id:str):
    cur.execute("DELETE FROM category WHERE id= %s;", (category_id,))
    conn.commit()
    return {"message": "Category successfully deleted"}

