# diplom_work
Пичугин Алексей ИУ9-81Б. Дипломная работа

## Что делать, если какой-то процесс запущен на нужном порту

lsof -i:"port_number" - покажет список процессов, запущенных на <port_number>

kill -9 "PID" - убить процесс с идентификатором PID

## Работа с PostgreSql

Запуск postgresql: pg_ctl -D /opt/homebrew/var/postgresql@14 start. 

brew install postgresql - если не запускается.

Если на debian пишет ошибку: psql: error: FATAL:  role "root" does not exist. То нужно делать следующее:

sudo -u postgres createuser -s root

\c database_name - зайти в базу database_name, после этого можно посмотреть какие таблицы в ней лежат

\dt - список таблиц в базе данных

### Установка возможности использования русского языка в данных

ALTER DATABASE diplom_work SET client_encoding TO 'UTF8';

ALTER DATABASE diplom_work SET default_text_search_config TO 'pg_catalog.russian';

### Создание пользователя, у которого будет бд сервиса, и базы данных сервиса 

psql postgres - Заходим в postgresql под дефолтным пользователем

CREATE USER pichugin_IU9 WITH ENCRYPTED PASSWORD 'IU9_one_love'; - создаём нового пользователя с именем pichugin_IU9 и паролем IU9_one_love

ALTER USER pichugin_iu9 WITH SUPERUSER; - даём все права (создание, изменение бд и тд) вновь созданному пользователю

\q - выйти из окна psql

psql -U pichugin_iu9 postgres - заходим под новым логином, вводим пароль, который создали до этого

create database diplom_work; - создаём базу данных сервиса

## Запуск back_end_server

python3 init_db.py - создание таблица в базе данных, которая была создана в предыдущем пункте

python3 main.py - запуск самого сервера
