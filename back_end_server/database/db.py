import psycopg2
from typing import Union, Tuple

remote_db_config = {
    'dbname': 'diplom_work',
    'user': 'postgres',
    'password': '123',
    'host': 'localhost'
}

local_db_config = {
    'dbname': 'diplom_work',
    'user': 'pichugin_iu9',
    'password': 'IU9_one_love',
    'host': 'localhost'
}

def get_db_connection():
    conn = psycopg2.connect(**remote_db_config)
    return conn

def execute_select_one_query(query: str):
    with get_db_connection().cursor() as cursor:
        cursor.execute(query)
        entry = cursor.fetchone()
        return entry

def execute_select_all_query(query: str):
    with get_db_connection().cursor() as cursor:
        cursor.execute(query)
        entry = cursor.fetchall()
        return entry

def execute_many_queries_without_response(queries):
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            for query in queries:
                cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        conn.rollback()
        print(e)
        return False

def insert(table_name: str, entry: dict):
    column_names = ', '.join([k for k in entry.keys()])
    values = ', '.join('%s' for _ in entry.keys())
    query = 'INSERT INTO {}({}) VALUES ({})'.format(table_name, column_names, values)
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, list(entry.values()))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
        return False
    return True

def update_one_record(table_name: str, fields: dict, condition: str):
    sets = ', '.join([k + ' = %s' for k in fields.keys()])
    query = 'UPDATE {} SET {} WHERE {}'.format(table_name, sets, condition)
    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, list(fields.values()))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
        return False
    return True

def insert_one_entry_and_return_inserted_id(table_name: str, entry: dict):
    column_names = ', '.join([k for k in entry.keys()])
    values = ', '.join('%s' for _ in entry.keys())
    query = 'INSERT INTO {}({}) VALUES ({}) RETURNING id'.format(table_name, column_names, values)
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(query, list(entry.values()))
        conn.commit()
        return cursor.fetchone()[0]
    except Exception as e:
        conn.rollback()
        print(e)
        return False
