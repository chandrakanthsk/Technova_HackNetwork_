"""
Configuration File
Stores all device and application settings.
"""

# Cisco Switch Details
DEVICE = {
    "device_type": "cisco_ios",
    "host": "192.168.1.10",      # Change later
    "username": "admin",         # Change later
    "password": "cisco",         # Change later
}

# Polling Interval (seconds)
POLL_INTERVAL = 30

# Baseline File
BASELINE_FILE = "baseline.json"

# Database File
DATABASE_FILE = "topology.db"