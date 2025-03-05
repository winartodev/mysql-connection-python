import mysql.connector 
import random
from datetime import date

try:
    mydb = mysql.connector.connect(
        host="127.0.0.1", 
        user="root", 
        password="123", 
        database="db_employee"
    )

    mysqlcursor = mydb.cursor()

    def generate_employee_data():
        names = ["Budi", "Ani", "Citra", "Dedi", "Eka", "Faisal", "Gita", "Hadi", "Indah", "Joko"]
        departments = ["Penjualan", "Pemasaran", "Teknik", "SDM", "Keuangan"]

        name = random.choice(names)
        department = random.choice(departments)

        return name, department

    for _ in range(10):
        name, department = generate_employee_data()
        sql = "INSERT INTO tbl_employee (name, department) VALUES (%s, %s)"
        val = (name, department)
        try:
            mysqlcursor.execute(sql, val)
        except mysql.connector.Error as err:
            print(f"Error inserting data: {err}")
            mydb.rollback()
            break

    mydb.commit()
    print(f"{mysqlcursor.rowcount} records inserted.")

    mysqlcursor.execute("SELECT * FROM tbl_employee") 
    myresult = mysqlcursor.fetchall()

    for x in myresult:
        print(x)
except mysql.connector.Error as err:
    print(f"Database connection or operation error: {err}")
finally:
    if mydb.is_connected():
        mysqlcursor.close()
        mydb.close()
        print("Database connection closed.")