from database.db_manager import connect

def insert_department(name):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO Departments (name) VALUES (?)', (name,))
    
    conn.commit()
    conn.close()

def get_all_departments():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Departments')

    rows = cursor.fetchall()
    conn.close()
    return rows
