from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

engine = create_engine("postgresql://postgres:{serverPasswordGoesHere}@localhost/product_db", echo = True)
sessionLocal = sessionmaker(bind=engine)

# newproduct= Product(product_id=1, product_name="eggs", product_price=300,product_delivery= False)
