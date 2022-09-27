from sqlalchemy import Column, String, Integer, Boolean
from database import Base

class Product(Base):
    __tablename__ = 'Products'
    product_id = Column(Integer(), unique =True, nullable =False, primary_key = True)
    product_name =Column(String(15), unique = True, nullable = False)
    product_price =Column(Integer(), nullable= False)
    product_delivery = Column(Boolean, default= False)
    
    def __repr__(self):
        return f'<Product product_id={self.product_id}, product_name= {self.product_name}, product_price ={self.product_price}, product_delivery={self.product_delivery}>'
    
