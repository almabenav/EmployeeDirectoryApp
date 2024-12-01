from models.employee import insert_employee, get_all_employees, update_employee, delete_employee
from models.department import insert_department, get_all_departments
from database.db_manager import create_tables

def main_menu():
    while True:
        print("\nEmployee Directory")
        print("1. Add Department")
        print("2. Add Employee")
        print("3. View All Employees")
        print("4. View All Departments")
        print("5. Update Employee")
        print("6. Delete Employee")
        print("0. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter department name: ")
            insert_department(name)
        elif choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            department_id = int(input("Enter department ID: "))
            date_hired = input("Enter date hired (YYYY-MM-DD): ")
            insert_employee(first_name, last_name, email, department_id, date_hired)
        elif choice == '3':
            employees = get_all_employees()
            for emp in employees:
                print(f"ID: {emp[0]}, Name: {emp[1]} {emp[2]}, Email: {emp[3]}, Department: {emp[4]}, Date Hired: {emp[5]}")
        elif choice == '4':
            departments = get_all_departments()
            for dep in departments:
                print(f"ID: {dep[0]}, Department Name: {dep[1]}")
        elif choice == '5':
            employee_id = int(input("Enter employee ID: "))
            first_name = input("Enter new first name: ")
            last_name = input("Enter new last name: ")
            email = input("Enter new email: ")
            department_id = int(input("Enter new department ID: "))
            date_hired = input("Enter new date hired (YYYY-MM-DD): ")
            update_employee(employee_id, first_name, last_name, email, department_id, date_hired)
        elif choice == '6':
            employee_id = int(input("Enter employee ID to delete: "))
            delete_employee(employee_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    # Ensure tables are created before starting the app
    create_tables()
    main_menu()
