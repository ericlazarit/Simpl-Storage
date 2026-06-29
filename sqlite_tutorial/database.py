import sqlite3
import os

def get_connection():
    db_path = os.path.join(os.path.dirname(__file__), 'discord_files.db')
    connection = sqlite3.connect(db_path)
    return connection

def init_db():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""
               CREATE TABLE IF NOT EXISTS discord_files(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id VARCHAR(30),
                   file_name TEXT,
                   file_type TEXT, 
                   upload_time DATE,
                   storage_path VARCHAR
               )
               """)
    connection.commit()


