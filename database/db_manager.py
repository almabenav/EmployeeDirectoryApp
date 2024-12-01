import sqlite3

DB_NAME = 'employee_directory.db'

def connect():
    """Establish a connection to the SQLite database."""
    return sqlite3.connect(DB_NAME)

def create_tables():
    """Create Employees and Departments tables if they do not exist."""
    conn = connect()
    cursor = conn.cursor()

    # Create the Employees table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        department_id INTEGER,
                        date_hired TEXT NOT NULL,
                        FOREIGN KEY(department_id) REFERENCES Departments(id)
                    )''')

    # Create the Departments table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Departments (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL
                    )''')

    conn.commit()
    conn.close()
