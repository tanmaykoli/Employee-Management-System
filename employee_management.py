import mysql.connector

# Connect to MySQL Database
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql123",
    database="emp"
)

cursor = con.cursor()

def add_employee():
    name = input("Enter employee name: ")
    position = input("Enter employee position: ")
    salary = float(input("Enter employee salary: "))

    cursor.execute(
        "INSERT INTO employees (name, position, salary) VALUES (%s, %s, %s)",
        (name, position, salary)
    )
    con.commit()
    print("✅ Employee added successfully")

def remove_employee():
    emp_id = int(input("Enter employee ID to remove: "))
    cursor.execute("DELETE FROM employees WHERE emp_id = %s", (emp_id,))
    con.commit()
    print("✅ Employee removed successfully")

def promote_employee():
    emp_id = int(input("Enter employee ID to promote: "))
    position = input("Enter new position: ")
    salary = float(input("Enter new salary: "))

    cursor.execute(
        "UPDATE employees SET position=%s, salary=%s WHERE emp_id=%s",
        (position, salary, emp_id)
    )
    con.commit()
    print("✅ Employee promoted successfully")

def display_employees():
    cursor.execute("SELECT * FROM employees")
    records = cursor.fetchall()

    if not records:
        print("\n❌ No employees found\n")
        return
    
    print("\nID | Name           | Position        | Salary")
    print("-----------------------------------------------")

    for emp in records:
        print(f"{emp[0]:<3}| {emp[1]:<14}| {emp[2]:<15}| {emp[3]}")

while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. Remove Employee")
    print("3. Promote Employee")
    print("4. Display Employees")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_employee()
    elif choice == '2':
        remove_employee()
    elif choice == '3':
        promote_employee()
    elif choice == '4':
        display_employees()
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice")
