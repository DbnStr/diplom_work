from database.db import execute_many_queries_without_response
from database.db import insert

def create_all_tables():
    queries = [

        #Создание таблицы со всеми покупателями (Consumer)
        "DROP TABLE IF EXISTS Consumer CASCADE;",
        """
            CREATE TABLE IF NOT EXISTS Consumer (
                id SERIAL PRIMARY KEY NOT NULL,
                name VARCHAR(100) NOT NULL,
                surname VARCHAR(100) NOT NULL)
        """,

        #Создание таблицы со всеми магазинами (Shop)
        "DROP TABLE IF EXISTS Shop CASCADE;",
        """
            CREATE TABLE IF NOT EXISTS Shop (
                id SERIAL PRIMARY KEY NOT NULL,
                name VARCHAR(100) NOT NULL)
        """,

        # Создание таблицы Пользователей внутри магазинов (ConsumerInShop)
        "DROP TABLE IF EXISTS ConsumerInShop CASCADE;",
        """
            CREATE TABLE IF NOT EXISTS ConsumerInShop (
                id SERIAL PRIMARY KEY NOT NULL,
                loyaltyId INT NOT NULL,
                consumerId INT NOT NULL REFERENCES Consumer (id),
                shopId INT NOT NULL REFERENCES Shop (id))
        """,

        #Создание таблицы корзин (Basket)
        "DROP TABLE IF EXISTS Basket CASCADE;",
        """
            CREATE TABLE IF NOT EXISTS Basket (
                id SERIAL PRIMARY KEY NOT NULL,
                idInShop INT NOT NULL,
                callbackURL VARCHAR(100) NOT NULL,
                totalAmount FLOAT4 NOT NULL,
                totalAmountWithDiscounts FLOAT4 NOT NULL,
                shopId INT NOT NULL REFERENCES Shop (id),
                consumerId INT NULL REFERENCES Consumer (id))
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
            CREATE TABLE IF NOT EXISTS ItemInBasket (
                id SERIAL PRIMARY KEY NOT NULL,
                quantity INT NOT NULL,
                amount FLOAT4 NOT NULL,
                basketId INT NOT NULL REFERENCES Basket (id),
                itemId INT NOT NULL REFERENCES Item (id))
        """,

        #Создание таблицы счетов (Invoice)
        "DROP TABLE IF EXISTS Invoice CASCADE;",
        """
            CREATE TABLE IF NOT EXISTS Invoice (
                id SERIAL PRIMARY KEY NOT NULL,
                amount FLOAT4 NOT NULL,
                paymentMethods VARCHAR(100) NOT NULL,
                expiredDateTime TIMESTAMP WITHOUT TIME ZONE NOT NULL,
                status VARCHAR(10) NOT NULL,
                basketId INT NOT NULL REFERENCES Basket (id),
                consumerId INT NOT NULL REFERENCES Consumer (id),
                shopId INT NOT NULL REFERENCES Shop (id))
        """,

        #Создание таблицы платежей (Payment)
        "DROP TABLE IF EXISTS Payment CASCADE;",
        """
            CREATE TABLE IF NOT EXISTS Payment (
                id SERIAL PRIMARY KEY NOT NULL,
                paymentMethod VARCHAR(10) NOT NULL,
                cardNumber VARCHAR(16) NOT NULL,
                paymentDateTime TIMESTAMP WITHOUT TIME ZONE NOT NULL,
                invoiceId INT NOT NULL REFERENCES Invoice (id))
        """
    ]
    execute_many_queries_without_response(queries)

def fill_items():
    items = [
        {
            "name": "Кефир Домик в деревне 3.2%, 900мл",
            "cost": 95
        },
        {
            "name": "Evervess Пленительный Апельсин 0,25л",
            "cost": 110
        },
        {
            "name": "Чай Ahmad Strawberry",
            "cost": 159.99
        },
        {
            "name": "Chester's Cherry 5%, 450мл",
            "cost": 104.99
        },
        {
            "name": "Палочки кукурузные Cheetos Сыр, 50г",
            "cost": 46.99
        },
        {
            "name": "Шоколад молочный Алёнка, 200г",
            "cost": 219.99
        },
    ]

    for i in items:
        insert("Item", i)

def fill_consumers():
    insert("Consumer", {"name": "Alexey", "surName": "Pichugin"})

def fill_shops():
    insert("Shop", {"name": "Pyaterochka"})

def fill_consumers_in_shops():
    insert("ConsumerInShop", {"loyaltyId": 123, "consumerId": 1, "shopId": 1})

if __name__ == "__main__":
    create_all_tables()
    fill_consumers()
    fill_shops()
    fill_consumers_in_shops()
    fill_items()
