# ============================================================
#  Database Operations
#  Simulates Dataverse / Common Data Service CRUD operations
# ============================================================

import mysql.connector
from config import DB_CONFIG


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def get_employee(emp_id):
    """Fetch employee details and leave balance from database."""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees WHERE emp_id = %s", (emp_id,))
    employee = cursor.fetchone()
    cursor.close()
    conn.close()
    return employee


def update_leave_balance(emp_id, days_used):
    """Deduct approved leave days from employee balance."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE employees SET used_leaves = used_leaves + %s WHERE emp_id = %s",
        (days_used, emp_id)
    )
    conn.commit()
    cursor.close()
    conn.close()


def log_request(emp_id, leave_type, start_date, end_date, days, reason, status):
    """Log the leave request and its decision to the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO leave_requests
           (emp_id, leave_type, start_date, end_date, days_requested, reason, status)
           VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        (emp_id, leave_type, start_date, end_date, days, reason, status)
    )
    conn.commit()
    cursor.close()
    conn.close()


def get_all_requests():
    """Fetch all leave requests — used by REST API."""
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT lr.*, e.name, e.department
        FROM leave_requests lr
        JOIN employees e ON lr.emp_id = e.emp_id
        ORDER BY lr.processed_at DESC
    """)
    requests = cursor.fetchall()
    cursor.close()
    conn.close()
    return requests
