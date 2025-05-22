import sqlite3
import csv

def init_db():
    conn = sqlite3.connect("errors.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS errors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            error_code TEXT,
            message TEXT,
            severity TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_error(timestamp, error_code, message, severity):
    conn = sqlite3.connect("errors.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO errors (timestamp, error_code, message, severity) VALUES (?, ?, ?, ?)",
                   (timestamp, error_code, message, severity))
    conn.commit()
    conn.close()

def get_all_errors():
    conn = sqlite3.connect("errors.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, error_code, message, severity FROM errors ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def clear_errors():
    conn = sqlite3.connect("errors.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM errors")
    conn.commit()
    conn.close()

def reset_errors():
    conn = sqlite3.connect("errors.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE errors SET severity = 'OK'")
    conn.commit()
    conn.close()

def export_errors(file_path="exported_errors.csv"):
    conn = sqlite3.connect("errors.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM errors")
    rows = cursor.fetchall()
    conn.close()

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Timestamp", "Error Code", "Message", "Severity"])
        writer.writerows(rows)

    print(f"✅ Logs exported to {file_path}")
