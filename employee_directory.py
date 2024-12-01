import sqlite3

# Connect to SQLite database, create one if it doesn't exist
conn = sqlite3.connect('employee_directory.db')

# Create a cursor object to interact with the database
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

# Commit and close the connection
conn.commit()
conn.close()
