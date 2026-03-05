# ============================================================
#  Flask REST API
#  Exposes automation engine via API endpoints
#  Simulates Power Platform custom connector integration
# ============================================================

from flask import Flask, jsonify
from automation import process_leave_requests
from db import get_all_requests, get_employee

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "app"      : "Leave Request Automation System",
        "version"  : "1.0",
        "endpoints": [
            "GET  /requests        — View all leave requests",
            "GET  /employee/<id>   — View employee details and leave balance",
            "POST /process         — Trigger the automation engine"
        ]
    })


@app.route('/requests', methods=['GET'])
def get_requests():
    """Fetch all leave requests from the database."""
    requests = get_all_requests()
    return jsonify(requests)


@app.route('/employee/<emp_id>', methods=['GET'])
def get_emp(emp_id):
    """Fetch employee details and remaining leave balance."""
    employee = get_employee(emp_id)
    if employee:
        employee['available_leaves'] = employee['total_leaves'] - employee['used_leaves']
        return jsonify(employee)
    return jsonify({"error": "Employee not found"}), 404


@app.route('/process', methods=['POST'])
def trigger_automation():
    """Trigger the full automation process."""
    try:
        process_leave_requests()
        return jsonify({
            "status" : "success",
            "message": "Automation completed successfully"
        })
    except Exception as e:
        return jsonify({
            "status" : "error",
            "message": str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True)
