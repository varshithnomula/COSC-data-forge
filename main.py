from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import os

# Define ORM base
Base = declarative_base()

# Define Category table
class Category(Base):
    __tablename__ = 'categories'
    category_id = Column(Integer, primary_key=True)
    category_name = Column(String, nullable=False)
    products = relationship("Product", back_populates="category")

# Define Product table
class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    product_name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.category_id'))
    category = relationship("Category", back_populates="products")

# Initialize SQLite3 database
db_file = 'products.db'
engine = create_engine(f'sqlite:///{db_file}', echo=False)
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Check if database is already populated
if not session.query(Category).first():
    # Add sample categories
    electronics = Category(category_name="Electronics")
    books = Category(category_name="Books")
    session.add_all([electronics, books])
    session.flush()

    # Add sample products
    session.add_all([
        Product(product_name="Smartphone", price=699.99, category_id=electronics.category_id),
        Product(product_name="Laptop", price=1299.49, category_id=electronics.category_id),
        Product(product_name="Python Crash Course", price=44.95, category_id=books.category_id),
    ])
    session.commit()

# Retrieve and print product details
for product in session.query(Product).join(Category).all():
    print(f"{product.product_name} - ${product.price} [{product.category.category_name}]")

session.close()
