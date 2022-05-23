import sqlite3


def get_employees():
    """

    :return: list of dictionaries
    """
    conn = sqlite3.connect('employees.db')
    cur = conn.cursor()
    sql = "SELECT gender, id FROM employees ORDER BY id"
    cur.execute(sql)
    rows = cur.fetchall()

    employees = []
    for row in rows:
        employee = {}
        employee["gender"] = row[0]
        employee["id"] = row[1]
        employees.append(employee)
    return employees
