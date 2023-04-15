# diplom_work
Пичугин Алексей ИУ9-81Б. Дипломная работа 

## Работа с PostgreSql

Запуск postgresql: pg_ctl -D /opt/homebrew/var/postgresql@14 start. 

brew install postgresql - если не запускается.

Если на debian пишет ошибку: psql: error: FATAL:  role "root" does not exist. То нужно делать следующее:

sudo -u postgres createuser -s root

### Создание пользователя, у которого будет бд сервиса, и базы данных сервиса 

psql postgres - Заходим в postgresql под дефолтным пользователем

CREATE USER pichugin_IU9 WITH ENCRYPTED PASSWORD 'IU9_one_love'; - создаём нового пользователя с именем pichugin_IU9 и паролем IU9_one_love

ALTER USER pichugin_iu9 WITH SUPERUSER; - даём все права (создание, изменение бд и тд) вновь созданному пользователю

\q - выйти из окна psql

psql -U pichugin_iu9 postgres - заходим под новым логином, вводим пароль, который создали до этого

create database diplom_work; - создаём базу данных сервиса

## Структура данных
Структура корзины:
```
{
 "id": "123", // Идентификатор корзины
 "items": [
   {
     "name": "Coca Cola", // название позиции
     "quantity": 12, // Количество товаров этой позиции
     "one_item_cost": 100, // Стоимость одной единицы товара
     "amount": 1200
   }
   ...
 ]
}
```
