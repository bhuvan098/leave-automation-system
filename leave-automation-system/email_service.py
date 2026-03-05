# ============================================================
#  Email Notification Service
#  Simulates Power Automate email action
# ============================================================

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_CONFIG


def send_notification(to_email, employee_name, status, days, start_date, end_date):
    """Send automated email notification to employee after decision."""

    subject = f"Leave Request {status} — Automated Notification"

    if status == "APPROVED":
        body = f"""
Dear {employee_name},

Your leave request has been APPROVED.

Details:
- Duration : {start_date} to {end_date} ({days} days)
- Status   : APPROVED

This is an automated notification from the Leave Management System.
        """
    else:
        body = f"""
Dear {employee_name},

Your leave request has been REJECTED.

Reason        : Insufficient leave balance.
Days Requested: {days}

Please contact HR for more information.

This is an automated notification from the Leave Management System.
        """

    msg = MIMEMultipart()
    msg['From']    = EMAIL_CONFIG['sender_email']
    msg['To']      = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.starttls()
        server.login(EMAIL_CONFIG['sender_email'], EMAIL_CONFIG['sender_password'])
        server.sendmail(EMAIL_CONFIG['sender_email'], to_email, msg.as_string())
        server.quit()
        print(f"  Email sent to {to_email}")
    except Exception as e:
        print(f"  Email failed: {e}")
