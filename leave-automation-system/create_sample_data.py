import openpyxl
import os

os.makedirs('data', exist_ok=True)

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Leave Requests"

# Headers
ws.append(['emp_id', 'leave_type', 'start_date', 'end_date', 'days_requested', 'reason'])

# Sample data — dates as strings
ws.append(['EMP001', 'Casual Leave',  '2026-03-10', '2026-03-12', 3, 'Personal work'])
ws.append(['EMP002', 'Sick Leave',    '2026-03-13', '2026-03-17', 5, 'Medical appointment'])
ws.append(['EMP003', 'Annual Leave',  '2026-03-20', '2026-03-21', 2, 'Family function'])

wb.save('data/leave_requests.xlsx')
print("Sample Excel file created at data/leave_requests.xlsx")
```

Then run these two commands one by one:
```
python create_sample_data.py
```
```
python automation.py