from fastapi import FastAPI, status
from pydantic import BaseModel
from db_service import get_products, update_product, delete_product, delete_category, get_category, post_category, post_product

app = FastAPI()

class Product(BaseModel):
    name: str
    price: int
    unit: str
    category_name: str

class ProductResponse(BaseModel):
    pass
@app.get("/products")

# PRODUCT API's
@app.get("/products")
async def read_products():
    return get_products()
@app.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def add_pro(product: Product):
    new_product = product.dict()
    return post_product(new_product["name"],new_product["price"],new_product["unit"],new_product["category_name"])
@app.delete("/products/{product_id}")
async def del_pro(product_id: str):
    return delete_product(product_id)
@app.put("/products/{product_id}",response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def update_pro(product_id:int, product: Product):
    new_product = product.dict()
    return update_product(product_id,new_product['name'],new_product['price'],new_product['unit'],new_product['category_name'])


# CATEGORY API's
@app.get("/categories")
async def read_categories():
    return get_category()
@app.post("/categories")
async def post_categories(name: str):
    return post_category(name)
@app.delete("/category/{category_id}")
async def del_category(category_id:str):
    return delete_category(category_id)