import sqlite3

conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("DELETE FROM EMPLOYEES WHERE ID=6")
conn.commit()
cursor=conn.execute("SELECT * FROM EMPLOYEES EMPLOYEES")

for row in cursor:
    print("ID",row[0])
    print("NAME",row[1])
    print("AGE",row[2])
    print("SALARY",row[3])

print("Records found")
conn.close()