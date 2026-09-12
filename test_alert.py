import sqlite3
from datetime import datetime

connection = sqlite3.connect("network_monitor.db")
cursor = connection.cursor()

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Insert a simulated DOWN alert
cursor.execute("""
INSERT INTO network_logs
(timestamp, host, status, packet_loss, latency, event)
VALUES (?, ?, ?, ?, ?, ?)
""", (
    current_time,
    "TEST-HOST",
    "OFFLINE",
    "100%",
    "N/A",
    "DOWN"
))

# Insert a simulated RECOVERED alert
cursor.execute("""
INSERT INTO network_logs
(timestamp, host, status, packet_loss, latency, event)
VALUES (?, ?, ?, ?, ?, ?)
""", (
    current_time,
    "TEST-HOST",
    "ONLINE",
    "0%",
    "5 ms",
    "RECOVERED"
))

connection.commit()
connection.close()

print("Test DOWN and RECOVERED alerts inserted successfully.")