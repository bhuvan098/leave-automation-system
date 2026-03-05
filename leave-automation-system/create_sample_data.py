import openpyxl
from datetime import date
import os

os.makedirs('data', exist_ok=True)

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Leave Requests"

# Headers
ws.append(['emp_id', 'leave_type', 'start_date', 'end_date', 'days_requested', 'reason'])

# Sample data
ws.append(['EMP001', 'Casual Leave',  date(2026, 3, 10), date(2026, 3, 12), 3, 'Personal work'])
ws.append(['EMP002', 'Sick Leave',    date(2026, 3, 13), date(2026, 3, 17), 5, 'Medical appointment'])
ws.append(['EMP003', 'Annual Leave',  date(2026, 3, 20), date(2026, 3, 21), 2, 'Family function'])

wb.save('data/leave_requests.xlsx')
print("Sample Excel file created at data/leave_requests.xlsx")
