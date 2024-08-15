import sqlite3
import pandas as pd

def connect_to_db(db_name="TestSecurityDB.sqlite"):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as err:
        print(f"Error: {err}")
        return None

def configuration_check(cursor):
    print("Performing configuration checks...")

    # Check the SQLite version.
    query = "SELECT sqlite_version();"
    cursor.execute(query)
    version = cursor.fetchone()

    results = {"SQLite Version": version[0]} 
    print("Configuration Check Results:", results)
    return results

def schema_audit(cursor):
    print("Performing schema audit...")

    # Retrieve all tables and their creation SQL
    query = "SELECT name, sql FROM sqlite_master WHERE type='table';"
    cursor.execute(query)
    tables = cursor.fetchall()
    print("Schema Audit Tables Found:", tables)

    schema_issues = []

    for table_name, table_sql in tables:
        if 'PRIMARY KEY' not in table_sql:
            schema_issues.append(f"Table {table_name} does not have a primary key.")

        if 'FOREIGN KEY' in table_sql:
            schema_issues.append(f"Table {table_name} has foreign keys defined.")
    
    print("Schema Issues Found:", schema_issues)
    return tables, schema_issues

def data_integrity_audit(cursor):
    print("Performing data integrity audit...")

    # Check foreign key constraints
    cursor.execute("PRAGMA foreign_key_check;")
    foreign_key_issues = cursor.fetchall()
    print("Foreign Key Issues:", foreign_key_issues)

    # Check for NULL constraints
    cursor.execute("""
    SELECT name, sql FROM sqlite_master 
    WHERE type='table' AND sql LIKE '%NOT NULL%';
    """)
    not_null_issues = cursor.fetchall()
    print("NOT NULL Issues:", not_null_issues)

    return foreign_key_issues, not_null_issues

def user_permissions_audit(cursor):
    print("Auditing user permissions...")

    # we will audit the Users table.
    query = "SELECT * FROM Users;"
    cursor.execute(query)
    users = cursor.fetchall()
    print("User Permissions Audit:", users)

    return users

def encryption_check(cursor):
    print("Checking data encryption practices...")

    # SQLite does not support native encryption without extensions like SQLCipher.
    # This check will simply note the absence of native encryption support.
    encryption_status = "No native encryption in SQLite without extensions."
    results = {"Encryption Supported": encryption_status}
    print("Encryption Check:", results)  # Debugging

    return results

def generate_report(configuration_results, schema_results, schema_issues, integrity_results, user_permissions, encryption_results):
    print("Generating report...")

    # Creating dataframes for each section
    config_df = pd.DataFrame([configuration_results])
    schema_df = pd.DataFrame(schema_results, columns=["Table Name", "Table Definition"])
    schema_issues_df = pd.DataFrame(schema_issues, columns=["Schema Issues"])
    foreign_key_df = pd.DataFrame(integrity_results[0], columns=["Table", "Row ID", "Referenced Table", "Foreign Key"])
    not_null_df = pd.DataFrame(integrity_results[1], columns=["Table Name", "Table Definition"])
    users_df = pd.DataFrame(user_permissions, columns=["ID", "Username", "Password", "Email", "Role", "Created At"])
    encryption_df = pd.DataFrame([encryption_results])

    # Writing the report to Excel
    with pd.ExcelWriter('SQLite_Security_Audit_Report.xlsx') as writer:
        config_df.to_excel(writer, sheet_name='Configuration_Checks', index=False)
        schema_df.to_excel(writer, sheet_name='Schema_Audit', index=False)
        schema_issues_df.to_excel(writer, sheet_name='Schema_Issues', index=False)
        foreign_key_df.to_excel(writer, sheet_name='Foreign_Key_Issues', index=False)
        not_null_df.to_excel(writer, sheet_name='Not_Null_Issues', index=False)
        users_df.to_excel(writer, sheet_name='User_Permissions', index=False)
        encryption_df.to_excel(writer, sheet_name='Encryption_Checks', index=False)

    print("Report generated: SQLite_Security_Audit_Report.xlsx")

def main():
    # Connect to the database
    conn = connect_to_db()
    if not conn:
        return

    cursor = conn.cursor()

    # Perform the audits
    configuration_results = configuration_check(cursor)
    schema_results, schema_issues = schema_audit(cursor)
    integrity_results = data_integrity_audit(cursor)
    user_permissions = user_permissions_audit(cursor)
    encryption_results = encryption_check(cursor)

    # Generate the report
    generate_report(configuration_results, schema_results, schema_issues, integrity_results, user_permissions, encryption_results)

    # Close the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
