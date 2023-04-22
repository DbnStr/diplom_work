from database.db import execute_many_queries_without_response
from database.db import insert

def create_all_tables():
    queries = [
        #Создание таблицы со всеми покупателями (Consumer)
        "DROP TABLE IF EXISTS Consumer;",
        """
            CREATE TABLE IF NOT EXISTS Shop (
                id SERIAL PRIMARY KEY NOT NULL)
        """,

        #Создание таблицы со всеми магазинами (Shop)
        "DROP TABLE IF EXISTS Shop;",
        """
            CREATE TABLE IF NOT EXISTS Shop (
                id SERIAL PRIMARY KEY NOT NULL,
                name VARCHAR(100) NOT NULL)
        """,

        #Создание таблицы корзин (Basket)
        "DROP TABLE IF EXISTS Basket CASCADE;",
        """
            CREATE TABLE IF NOT EXISTS Basket (
                id SERIAL PRIMARY KEY NOT NULL,
                idInShop INT NOT NULL,
                shopId INT NOT NULL,
                consumerId INT NULL)
        """,

        # Создание таблицы Товаров - справочник товаров (Item)
        "DROP TABLE IF EXISTS Item CASCADE;",
        """
            CREATE TABLE IF NOT EXISTS Item (
                id SERIAL PRIMARY KEY NOT NULL,
                name VARCHAR(100) NOT NULL,
                cost FLOAT4 NOT NULL)
        """,

        #Создание таблицы Товаров внутри корзины (ItemInBasket)
        "DROP TABLE IF EXISTS ItemInBasket CASCADE;",
        """
            CREATE TABLE IF NOT EXISTS Item (
                id SERIAL PRIMARY KEY NOT NULL,
                quantity INT NOT NULL,
                amount FLOAT4 NOT NULL,
                basketId INT NOT NULL REFERENCES Basket (id),
                itemId INT NOT NULL REFERENCES Item (id))
        """]
    execute_many_queries_without_response(queries)

def fill_items():
    items = [
        {
            "name": "Coca cola 1.5l",
            "cost": 100
        },
        {
            "name": "Orbit Mint Gum",
            "cost": 50
        },
    ]

    for i in items:
        insert("Item", i)

if __name__ == "__main__":
    create_all_tables()
    fill_items()