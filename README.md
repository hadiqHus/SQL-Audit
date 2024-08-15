# SQLite Foreign Key Audit

This project demonstrates how to simulate and audit foreign key violations in an SQLite database using Python.

## Features

- **Database Setup:** Create a SQLite database with multiple tables and relationships (primary and foreign keys).
- **Foreign Key Violations:** Simulate foreign key violations by inserting invalid records.
- **Audit Script:** Check for foreign key violations and other database integrity issues, then generate an Excel report.

## Prerequisites

- Python 3.x
- SQLite (included with Python)
- [pandas](https://pandas.pydata.org/) for generating Excel reports

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/SQLite-Foreign-Key-Audit.git
    cd SQLite-Foreign-Key-Audit
    ```

2. (Optional) Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

## Usage

### 1. Set Up the Database

Run the `setup_database.py` script to create the database and populate it with data:

```bash
python setup_database.py
```
![image](https://github.com/user-attachments/assets/3a5f5e90-012c-422c-86ea-b9683cc064d6)

![image](https://github.com/user-attachments/assets/e76b1028-768d-421a-b45f-4b07635355e3)


## Example

![image](https://github.com/user-attachments/assets/7fb660b3-240d-44ba-b375-5a6b6b7e11d9)

![image](https://github.com/user-attachments/assets/44a573df-5960-4e85-aa7f-8fef03bdcae6)
