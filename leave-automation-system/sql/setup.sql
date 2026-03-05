-- ============================================================
--  Database Setup
--  Run this file first before running the project
--  Command: mysql -u root -p < sql/setup.sql
-- ============================================================

CREATE DATABASE IF NOT EXISTS leave_automation;
USE leave_automation;

-- ---- Employees Table ----
CREATE TABLE IF NOT EXISTS employees (
    emp_id       VARCHAR(10)  PRIMARY KEY,
    name         VARCHAR(100) NOT NULL,
    email        VARCHAR(100) NOT NULL,
    department   VARCHAR(50),
    total_leaves INT          DEFAULT 20,
    used_leaves  INT          DEFAULT 0
);

-- ---- Leave Requests Table ----
CREATE TABLE IF NOT EXISTS leave_requests (
    request_id    INT AUTO_INCREMENT PRIMARY KEY,
    emp_id        VARCHAR(10),
    leave_type    VARCHAR(50),
    start_date    DATE,
    end_date      DATE,
    days_requested INT,
    reason        TEXT,
    status        VARCHAR(20)  DEFAULT 'PENDING',
    processed_at  TIMESTAMP    DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

-- ---- Sample Employee Data ----
INSERT IGNORE INTO employees VALUES
('EMP001', 'Ravi Kumar',   'ravi@example.com',  'Engineering', 20, 5),
('EMP002', 'Priya Sharma', 'priya@example.com', 'HR',          20, 12),
('EMP003', 'Anil Reddy',   'anil@example.com',  'Finance',     20, 19);
