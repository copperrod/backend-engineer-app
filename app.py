from flask import Flask, jsonify
from db import get_employees
from sqlite3 import OperationalError

app = Flask(__name__)


@app.route('/employees', methods=['GET'])
def api_get_employees():
    try:
        employees = get_employees()
        return jsonify(employees)
    except OperationalError:
        return jsonify({"success": False, "message": "Error occurred while accessing employee data"}), 500
