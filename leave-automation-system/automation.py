# ============================================================
#  Automation Engine — Core Business Logic
#  Simulates a full Power Automate Desktop flow:
#  Trigger → Conditions → DB Operations → Notifications
# ============================================================

from db import get_employee, update_leave_balance, log_request
from email_service import send_notification
from excel_reader import read_leave_requests


def calculate_available_leaves(employee):
    """Calculate remaining leave balance."""
    return employee['total_leaves'] - employee['used_leaves']


def apply_business_rules(employee, days_requested):
    """
    Business rules engine.
    Simulates Power Automate condition blocks.

    Rule 1: Employee must exist in the system
    Rule 2: Days requested must be greater than 0
    Rule 3: Employee must have sufficient leave balance
    """
    if not employee:
        return False, "Employee not found in system"

    if days_requested <= 0:
        return False, "Invalid number of days requested"

    available = calculate_available_leaves(employee)
    if days_requested > available:
        return False, f"Insufficient balance. Available: {available}, Requested: {days_requested}"

    return True, "Approved"


def process_leave_requests():
    """
    Main automation engine.

    Flow:
    1. Read requests from Excel     (simulates PAD trigger)
    2. Fetch employee from DB       (simulates Dataverse lookup)
    3. Apply business rules         (simulates PAD condition blocks)
    4. Update DB if approved        (simulates Dataverse write-back)
    5. Log request to DB            (simulates audit log)
    6. Send email notification      (simulates PAD email action)
    """
    print("=" * 55)
    print("  Leave Automation System — Process Started")
    print("=" * 55)

    requests = read_leave_requests()
    print(f"\n  Found {len(requests)} pending request(s)\n")

    for req in requests:
        print(f"  Processing : {req['emp_id']} | {req['leave_type']} | {req['days']} days")

        # Step 1: Fetch employee from database
        employee = get_employee(req['emp_id'])

        # Step 2: Apply business rules
        approved, message = apply_business_rules(employee, req['days'])

        # Step 3: Determine status
        status = "APPROVED" if approved else "REJECTED"

        # Step 4: Update leave balance if approved
        if approved:
            update_leave_balance(req['emp_id'], req['days'])

        # Step 5: Log request to database
        log_request(
            req['emp_id'], req['leave_type'],
            req['start_date'], req['end_date'],
            req['days'], req['reason'], status
        )

        # Step 6: Send email notification
        send_notification(
            employee['email'], employee['name'],
            status, req['days'],
            req['start_date'], req['end_date']
        )

        print(f"  Result     : {status} — {message}\n")

    print("=" * 55)
    print("  Automation Complete.")
    print("=" * 55)


if __name__ == "__main__":
    process_leave_requests()
