import psycopg2
import datetime
import time


con = None

try:
    conn = psycopg2.connect("dbname='todo_manager' user='csetuser' host='127.0.0.1' password='Screenprinter1!'")

except:
    print("I am unable to connect to the database")

cur = conn.cursor()
try:
    cur.execute("""SELECT * from task_list""")
except:
    print("I can't SELECT from task_list")

rows = cur.fetchall()
print("\nRows: \n")
for row in rows:
    # row[2] == datetime.date.strftime("%Y-%m-%d %H:%M:%S")
    print("   ", row)
