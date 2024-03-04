import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (11,'faith karimi',26,450000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (12,'job richard',26,390000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (13,'ali john',26,2000000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (14,' nolan jade',26,300000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (16,'job harrison',35,3450000.00)")
conn.commit()
print("Records inserted successfully")
conn.close()