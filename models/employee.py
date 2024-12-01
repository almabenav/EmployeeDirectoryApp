from database.db_manager import connect

def insert_employee(first_name, last_name, email, department_id, date_hired):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO Employees (first_name, last_name, email, department_id, date_hired)
                      VALUES (?, ?, ?, ?, ?)''',
                   (first_name, last_name, email, department_id, date_hired))
    
    conn.commit()
    conn.close()

def get_all_employees():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''SELECT Employees.id, first_name, last_name, email, Departments.name AS department, date_hired
                      FROM Employees
                      JOIN Departments ON Employees.department_id = Departments.id''')

    rows = cursor.fetchall()
    conn.close()
    return rows

def update_employee(employee_id, first_name, last_name, email, department_id, date_hired):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''UPDATE Employees
                      SET first_name = ?, last_name = ?, email = ?, department_id = ?, date_hired = ?
                      WHERE id = ?''',
                   (first_name, last_name, email, department_id, date_hired, employee_id))

    conn.commit()
    conn.close()

def delete_employee(employee_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Employees WHERE id = ?', (employee_id,))

    conn.commit()
    conn.close()
