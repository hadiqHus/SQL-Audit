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

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Set Up the Database

Run the `setup_database.py` script to create the database and populate it with data:

```bash
python setup_database.py
