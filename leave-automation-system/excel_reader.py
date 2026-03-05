# ============================================================
#  Excel Reader
#  Reads leave requests from Excel file
#  Simulates a Power Automate trigger (form submission / file trigger)
# ============================================================

import openpyxl


def read_leave_requests(filepath='data/leave_requests.xlsx'):
    """
    Read leave requests from Excel file.
    Simulates reading from a Power Automate trigger or form submission.

    Expected columns:
    emp_id | leave_type | start_date | end_date | days_requested | reason
    """
    wb = openpyxl.load_workbook(filepath)
    ws = wb.active

    requests = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        emp_id, leave_type, start_date, end_date, days, reason = row
        if emp_id:  # skip empty rows
            requests.append({
                'emp_id'    : emp_id,
                'leave_type': leave_type,
                'start_date': start_date,
                'end_date'  : end_date,
                'days'      : days,
                'reason'    : reason
            })
    return requests
