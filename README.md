# diplom_work
Пичугин Алексей ИУ9-81Б. Дипломная работа 

## Работа с PostgreSql

Запуск postgresql: pg_ctl -D /opt/homebrew/var/postgresql@14 start. 

brew install postgresql - если не запускается.

Если на debian пишет ошибку: psql: error: FATAL:  role "root" does not exist. То нужно делать следующее:

sudo -u postgres createuser -s root

\c database_name - Зайти в базу database_name, после этого можно посмотреть какие таблицы в ней лежат

### Создание пользователя, у которого будет бд сервиса, и базы данных сервиса 

psql postgres - Заходим в postgresql под дефолтным пользователем

CREATE USER pichugin_IU9 WITH ENCRYPTED PASSWORD 'IU9_one_love'; - создаём нового пользователя с именем pichugin_IU9 и паролем IU9_one_love

ALTER USER pichugin_iu9 WITH SUPERUSER; - даём все права (создание, изменение бд и тд) вновь созданному пользователю

\q - выйти из окна psql

psql -U pichugin_iu9 postgres - заходим под новым логином, вводим пароль, который создали до этого

create database diplom_work; - создаём базу данных сервиса

## Запуск back_end_server

python3 init_db.py - создание таблица в базе данных, которая была создана в предыдущем пункте

## Структура данных

POST запрос от магазина в back_end_server содержит корзины в формте JSON. Её структура описана ниже.


Структура корзины:
```
{
 "idInShop": 123, // Идентификатор корзины в магазине
 "shopId": 12, // Идентификатор магазина, публикующего корзину
 "items": [
   {
     "name": "Coca Cola", // название позиции
     "quantity": 12, // Количество товаров этой позиции
     "oneItemCost": 100, // Стоимость одной единицы товара
     "amount": 1200
   }
   ...
 ]
}
```
