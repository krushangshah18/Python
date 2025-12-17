import mysql.connector
import os

from dotenv import load_dotenv
load_dotenv()

conn = mysql.connector.connect(
    host="localhost",
    user=os.getenv('USERNM'),
    password=os.getenv('PASS'),
    database="myDB"
)
print("Connected to MySQL")

"""
Connection = phone line
Cursor = person speaking SQL on that line
You cannot execute SQL without a cursor
"""
cursor = conn.cursor()

#Create
query = """
INSERT INTO users (name)
VALUES (%s)
"""
values = ("Alice",)

cursor.execute(query, values)
conn.commit()   # VERY IMPORTANT
#INSERT / UPDATE / DELETE modify data, MySQL uses transactions : Without commit() → data is NOT saved
print("User inserted")

#Read
cursor.execute("SELECT id, name FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()