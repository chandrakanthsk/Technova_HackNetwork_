# database.py

import sqlite3
from datetime import datetime
from config import DATABASE_FILE


def create_database():
    """
    Create the alerts table if it does not already exist.
    """

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            change_type TEXT NOT NULL,
            local_device TEXT,
            remote_device TEXT,
            local_port TEXT,
            remote_port TEXT,
            risk TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()

    print("Database initialized successfully.")


def save_alert(event):
    """
    Save a topology change event to the database.
    """

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO alerts (
            timestamp,
            change_type,
            local_device,
            remote_device,
            local_port,
            remote_port,
            risk
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        timestamp,
        event["change_type"],
        event["local_device"],
        event["remote_device"],
        event["local_port"],
        event["remote_port"],
        event["risk"]
    ))

    connection.commit()
    connection.close()

    print("Alert saved to database.")


def get_alerts():
    """
    Get all stored alerts.
    """

    connection = sqlite3.connect(DATABASE_FILE)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM alerts
        ORDER BY id DESC
    """)

    alerts = cursor.fetchall()

    connection.close()

    return alerts


# Test
if __name__ == "__main__":

    create_database()

    sample_event = {
        "change_type": "NEW CONNECTION",
        "local_device": "Core-Switch",
        "remote_device": "Unknown-Switch",
        "local_port": "Gi0/2",
        "remote_port": "Gi0/1",
        "risk": "HIGH"
    }

    save_alert(sample_event)

    print("\n===== SAVED ALERTS =====")

    alerts = get_alerts()

    for alert in alerts:
        print(alert)