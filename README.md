# leave-automation-system
Business process automation system simulating Power Automate Desktop flow — Python, Flask, MySQL, REST API

# Employee Leave Request Automation System

A business process automation system built with Python that simulates an end-to-end Power Automate Desktop flow — from leave request intake to approval/rejection and email notification — without any manual intervention.

---

## 📌 Project Overview

This system automates the entire employee leave request process by connecting Excel data input, MySQL database operations, business rule evaluation, and automated email notifications into a single seamless workflow.

Built to demonstrate **business process automation**, **database integration**, **API development and integration**, and **workflow logic** — core skills required in Power Platform / PAD development roles.

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Flask | REST API endpoints |
| MySQL | Database — employee data and leave records |
| openpyxl | Read leave requests from Excel |
| smtplib | Automated email notifications |

---

## 🔁 Automation Workflow

```
Excel File (Leave Request Input)
        ↓
  Read Request (Trigger)
        ↓
  Fetch Employee from Database
        ↓
  Apply Business Rules (Conditions)
  ┌─────────────────────────────┐
  │ Rule 1: Employee exists?    │
  │ Rule 2: Days valid?         │
  │ Rule 3: Balance sufficient? │
  └─────────────────────────────┘
        ↓
  ┌──────────┬──────────┐
APPROVED    REJECTED
  │              │
  ↓              ↓
Update DB    Log Request
(Deduct      to Database
 Balance)
  │              │
  └──────┬───────┘
         ↓
  Send Email Notification
  to Employee
         ↓
  Process Complete
```

---

## 🗂️ Project Structure

```
leave-automation-system/
│
├── app.py                  → Flask REST API endpoints
├── automation.py           → Core automation engine (main workflow)
├── db.py                   → Database CRUD operations
├── email_service.py        → Email notification service
├── excel_reader.py         → Read leave requests from Excel
├── config.py               → DB and email configuration
├── create_sample_data.py   → Generate sample Excel input file
│
├── data/
│   └── leave_requests.xlsx → Input file (leave request data)
│
├── sql/
│   └── setup.sql           → Database schema and sample data
│
└── requirements.txt        → Project dependencies
```

---

## 🌐 REST API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | API overview and available endpoints |
| GET | `/requests` | Fetch all leave requests from database |
| GET | `/employee/<id>` | Fetch employee details and leave balance |
| POST | `/process` | Trigger the full automation engine |

---

## 🚀 How to Run

**Step 1** — Install dependencies
```
pip install -r requirements.txt
```

**Step 2** — Set up the database
```
mysql -u root -p < sql/setup.sql
```

**Step 3** — Update `config.py` with your database and Gmail credentials

**Step 4** — Generate sample input data
```
python create_sample_data.py
```

**Step 5** — Run automation directly
```
python automation.py
```

**Step 6** — Or run as REST API
```
python app.py
```
API available at `http://localhost:5000`

---

## 📊 Sample Output

```
=======================================================
  Leave Automation System — Process Started
=======================================================

  Found 3 pending request(s)

  Processing : EMP001 | Casual Leave | 3 days
  Email sent to ravi@example.com
  Result     : APPROVED — Approved

  Processing : EMP002 | Sick Leave | 5 days
  Email sent to priya@example.com
  Result     : REJECTED — Insufficient balance. Available: 8, Requested: 5

  Processing : EMP003 | Annual Leave | 2 days
  Email sent to anil@example.com
  Result     : REJECTED — Insufficient balance. Available: 1, Requested: 2

=======================================================
  Automation Complete.
=======================================================
```

---

## 🔗 JD Mapping — Cognizant PAD Developer

| JD Requirement | This Project |
|---|---|
| Business process flow development | End-to-end automated workflow — trigger → conditions → DB → notification |
| Dataverse / SQL / DB connection | MySQL CRUD operations — lookup, update, log |
| API development and integration | Flask REST API with 4 endpoints |
| Handle design document | This README serves as the technical design document |
| Define, design, configure, test, deploy | Full SDLC followed end to end |
| Reusable and reliable automation code | Modular structure — each file has one responsibility |
| Email / notification action | SMTP automated email notification to employee |

---

## 👨‍💻 Author

**Bestha Bhuvan**
B.Tech CSE (AI & ML) — SVCE Tirupati, 2026
[LinkedIn](https://linkedin.com/in/bhuvanbestha) | [GitHub](https://github.com/bhuvanbestha)
