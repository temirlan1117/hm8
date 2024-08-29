import sqlite3 as sql3
with sql3.connect('person.db') as connection:
    cursor = connection.cursor()
    # cursor.execute(''' create table if not exists Departaments(
    #  DepartmentID INTEGER PRIMARY KEY,
    #  DepartmentName TEXT NOT NULL
    # )''')
    # cursor.execute('''create table if not exists Employees(
    # employeeID INTEGER PRIMARY KEY,
    # FirstName TEXT NOT NULL,
    # LastName TEXT NOT NULL,
    # DepartmentID INTEGER,
    # FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
    # )''')
    # cursor.execute('''
    # INSERT INTO  Departaments VALUES (101, 'HR'), (102, 'IT'), (103, 'Sales')
    # ''')
    # cursor.execute('''
    # INSERT INTO Employees VALUES (1, 'John', 'Doe', 101), (2, 'Emily', 'Johnson', 102), (3, 'Chris', 'Brown', 103);''')
    cursor.execute('''
    SELECT 
    Employees.EmployeeID,
    Employees.FirstName,
    Employees.LastName,
    Departaments.DepartmentName
    FROM 
    Employees
    JOIN 
    Departaments ON Employees.DepartmentID = Departaments.DepartmentID;''')
    for row in cursor.fetchall():
        print(row)
        print()
    cursor.execute('''
    SELECT 
    EmployeeID,
    FirstName,
    LastName
    FROM 
    Employees
    WHERE 
    DepartmentID = (SELECT DepartmentID FROM Departaments WHERE DepartmentName = 'IT')
    ''')
    for row in cursor.fetchall():
        print(row)