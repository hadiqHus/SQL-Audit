import sqlite3

def simulate_foreign_key_violations(num_violations=50):
    conn = sqlite3.connect("TestSecurityDB.sqlite")
    cursor = conn.cursor()

    # Attempt to insert multiple records with non-existent user_id and project_id
    try:
        for i in range(num_violations):
            user_id = 9999 + i  # Generating unique non-existent user_id
            project_id = 9999 + i  # Generating unique non-existent project_id
            cursor.execute("""
                INSERT INTO UserProjects (user_id, project_id, role_on_project)
                VALUES (?, ?, ?)
            """, (user_id, project_id, 'Lead'))

        conn.commit()
        print(f"{num_violations} foreign key violations simulated successfully.")
    except sqlite3.IntegrityError as e:
        print(f"Integrity Error: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    simulate_foreign_key_violations(50)
