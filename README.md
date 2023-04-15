# diplom_work
Пичугин Алексей ИУ9-81Б. Дипломная работа 

## Работа с PostgreSql

Запуск postgresql: pg_ctl -D /opt/homebrew/var/postgresql@14 start
brew install postgresql - если не запускается
Зайти в BD для редактирования настроек ролей: psql postgres. postgres - мейн владелец.

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
