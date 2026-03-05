# ============================================================
#  Configuration File
#  Update DB and Email credentials before running
# ============================================================

# Database configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',   # change this
    'database': 'leave_automation'
}

# Email configuration (use Gmail App Password)
EMAIL_CONFIG = {
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'sender_email': 'your_email@gmail.com',   # change this
    'sender_password': 'your_app_password'    # use Gmail App Password
}
