import sqlite3
from db import queries
import config

def create_tables():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute(queries.tasks_table)
    conn.commit()
    conn.close()

def add_new_task(name):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute(queries.insert_tasks, (name,))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id

def edit_task(task_id, new_value):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute(queries.update_tasks, (new_value, task_id))
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute(queries.delete_tasks, (task_id,))
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute(queries.read_tasks)
    result = cursor.fetchall()
    conn.close()
    return result

def update_task_completed(task_id, completed):
    conn = sqlite3.connect(config.db_path)
    cursor = conn.cursor()
    cursor.execute(queries.update_completed, (completed, task_id))
    conn.commit()
    conn.close()