
# SQLite ORM Demo using SQLAlchemy

This project demonstrates how to use Python's SQLAlchemy ORM to:
- Connect to a SQLite3 database
- Create and define tables (`Category` and `Product`)
- Populate the database with sample data
- Retrieve and display data with relationships

## 📦 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
````

## ▶️ How to Run

```bash
python main.py
```

* This will:

  * Create `products.db` (if not already present)
  * Populate it with sample categories and products
  * Print product name, price, and category to the console

## 🗃️ Database Schema

**Category Table**

* `category_id` (Primary Key)
* `category_name` (Text)

**Product Table**

* `product_id` (Primary Key)
* `product_name` (Text)
* `price` (Float)
* `category_id` (Foreign Key → Category)

## 📂 Project Structure

```
sqlite-orm-demo/
├── main.py              # Main script for DB creation, data insertion, retrieval
├── products.db          # Auto-generated SQLite database file
├── requirements.txt     # Project dependencies
└── README.md            # Project overview and instructions
```

## 🧪 Sample Output

```
Smartphone - $699.99 [Electronics]
Laptop - $1299.49 [Electronics]
Python Crash Course - $44.95 [Books]
```

## 🛠️ Built With

* [Python 3.x](https://www.python.org/)
* [SQLAlchemy](https://www.sqlalchemy.org/)

