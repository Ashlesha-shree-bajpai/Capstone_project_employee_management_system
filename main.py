employees = []

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    
    employee = {
        "id": emp_id,
        "name": name,
        "dept": dept
    }
    
    employees.append(employee)
    print("✅ Employee added successfully!\n")


def view_employees():
    if not employees:
        print("⚠ No employees found.\n")
        return
    
    print("\nEmployee List:")
    for emp in employees:
        print(f"ID: {emp['id']} | Name: {emp['name']} | Dept: {emp['dept']}")
    print()


def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    
    for emp in employees:
        if emp["id"] == emp_id:
            emp["name"] = input("Enter new name: ")
            emp["dept"] = input("Enter new department: ")
            print("✅ Employee updated!\n")
            return
    
    print("❌ Employee not found.\n")


def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("✅ Employee deleted!\n")
            return
    
    print("❌ Employee not found.\n")


def menu():
    while True:
        print("===== Employee Management System =====")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice!\n")


menu()