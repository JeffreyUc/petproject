from http.client import HTTPException
from fastapi import FastAPI, status
from pydantic import BaseModel
from database import sessionLocal
from typing import List
import models

db = sessionLocal()

app = FastAPI()

class Product(BaseModel):
    product_id:int
    product_name:str
    product_price:int
    product_delivery:bool
    

@app.get('/products', response_model= List[Product], status_code= 200)
def get_all_products():
    products = db.query(models.Product).all()

@app.get('/products/{product_id}')
def get_a_product(product_id:int):
    product = db.query(models.Product).filter(models.Product.product_id== product_id).first()
    
    return product
    

@app.post('/product', response_model=Product, status_code= status.HTTP_201_CREATED)

def add_a_product(product:Product,):
    db_product = db.query(models.Product).filter(models.Product.product_name== new_product.product_name).first()
    if db_product is not None:
        raise HTTPException(status_code = 400, detail ='Product already exist')

    new_product = models.Product(
        product_id= product.product_id,
        product_name= product.product_name,
        product_price = product.product_price,
        product_delivery = product.product_delivery 
    )
    
    db.add(new_product)
    db.commit()

    return new_product

    

@app.put('/product/{product_id}', response_model=Product, status_code= status.HTTP_202_ACCEPTED)
def update_a_product(product_id:int, product:Product):
    product_to_update = db.query(models.Product).filter(models.Product.product_id == product_id).first()
    product_to_update.product_id = product.product_id
    product_to_update.product_name = product.product_name
    product_to_update.product_price = product.product_price
    product_to_update.product_delivery = product.product_delivery
    
    db.commit()
    
    return product_to_update
    


@app.delete('/product/{product_id}')
def delete_a_product(product_id:int):
    product_to_delete = db.query(models.Product).filter(models.Product.product_id == product_id).first()
    
    if product_to_delete is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
    
    db.delete(product_to_delete)
    db.commit()
    
    return product_to_delete
