import sqlite3
import random
import string

def connect_to_db(db_name="TestSecurityDB.sqlite"):
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_name)
    return conn

def create_tables(cursor):
    # Create the Users table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            role TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)


    # Create the Departments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Departments (
            department_id INTEGER PRIMARY KEY AUTOINCREMENT,
            department_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)


    # Create the Projects table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Projects (
            project_id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            department_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (department_id) REFERENCES Departments(department_id)
        )
    """)


    # Create the UserProjects table (many-to-many relationship)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS UserProjects (
            user_project_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            project_id INTEGER,
            role_on_project TEXT,
            assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES Users(id),
            FOREIGN KEY (project_id) REFERENCES Projects(project_id)
        )
    """)
    
    print("Tables 'Users', 'Departments', 'Projects', and 'UserProjects' created successfully.")

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def insert_random_users(cursor, num_users=20):
    roles = ['admin', 'editor', 'viewer']
    
    for _ in range(num_users):
        username = generate_random_string(8)
        password = generate_random_string(12)
        email = f"{username}@example.com"
        role = random.choice(roles)
        
        cursor.execute("""
            INSERT INTO Users (username, password, email, role)
            VALUES (?, ?, ?, ?)
        """, (username, password, email, role))
    
    print(f"{num_users} random users inserted successfully.")

def insert_departments_and_projects(cursor):
    departments = ['HR', 'Engineering', 'Marketing', 'Sales']
    for department in departments:
        cursor.execute("INSERT INTO Departments (department_name) VALUES (?);", (department,))
    
    # Create some projects associated with the departments
    projects = [('Website Revamp', 2), ('Product Launch', 3), ('Employee Training', 1), ('Client Outreach', 4)]
    for project_name, department_id in projects:
        cursor.execute("INSERT INTO Projects (project_name, department_id) VALUES (?, ?);", (project_name, department_id))
    
    print("Departments and projects inserted successfully.")

def insert_user_projects(cursor):
    user_ids = cursor.execute("SELECT id FROM Users").fetchall()
    project_ids = cursor.execute("SELECT project_id FROM Projects").fetchall()

    # Randomly assign users to projects
    for user_id in user_ids:
        for project_id in project_ids:
            if random.choice([True, False]):
                role_on_project = random.choice(['Lead', 'Contributor', 'Viewer'])
                cursor.execute("""
                    INSERT INTO UserProjects (user_id, project_id, role_on_project)
                    VALUES (?, ?, ?)
                """, (user_id[0], project_id[0], role_on_project))
    
    print("User-project associations inserted successfully.")

def main():
    # Connect to the database
    conn = connect_to_db()
    cursor = conn.cursor()

    # Create the tables
    create_tables(cursor)

    # Insert random users
    insert_random_users(cursor, 20)

    # Insert departments and projects
    insert_departments_and_projects(cursor)

    # Assign users to projects
    insert_user_projects(cursor)

    # Commit changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    print("Database setup with relationships completed.")

if __name__ == "__main__":
    main()
