import sqlite3

connection = sqlite3.connect('people_table')
cursor = connection.cursor()

cursor.execute("""
            CREATE TABLE IF NOT EXISTS people_table(
               name TEXT,
               age INTEGER
               )
 """)



eric_name = "Eric"
eric_age = 20

cursor.execute("INSERT INTO people_table(name,age) VALUES (?,?)", (eric_name, eric_age))
connection.commit()

result = cursor.execute("""  
            SELECT * FROM people_table   
 """)

print(result.fetchall())
connection.close()


