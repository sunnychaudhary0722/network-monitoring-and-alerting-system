import sqlite3

connection = sqlite3.connect("network_monitor.db")

cursor = connection.cursor()

cursor.execute("""
SELECT
    id,
    timestamp,
    host,
    status,
    packet_loss,
    latency,
    event
FROM network_logs
WHERE event IN ('DOWN', 'RECOVERED')
ORDER BY id DESC
LIMIT 10
""")

rows = cursor.fetchall()

print("\nRECENT ALERTS")
print("=" * 100)

if rows:

    for row in rows:
        print(row)

else:

    print("No DOWN or RECOVERED alerts found.")

print("=" * 100)

connection.close()