from flask import Flask, render_template
import sqlite3
import os
import sys

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

# Import monitored hosts from config.py
from config import HOSTS

DATABASE = os.path.join(BASE_DIR, "network_monitor.db")


def get_database_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def dashboard():

    connection = get_database_connection()

    placeholders = ",".join(["?"] * len(HOSTS))

    logs = connection.execute(
        f"""
        SELECT *
        FROM network_logs
        WHERE host IN ({placeholders})
        ORDER BY id DESC
        LIMIT 30
        """,
        HOSTS
    ).fetchall()


    hosts = []

    for host in HOSTS:

        row = connection.execute(
            """
            SELECT *
            FROM network_logs
            WHERE host = ?
            ORDER BY id DESC
            LIMIT 1
            """,
            (host,)
        ).fetchone()

        if row:
            hosts.append(row)

    statistics = []

    for host in HOSTS:

        total = connection.execute(
            """
            SELECT COUNT(*)
            FROM network_logs
            WHERE host = ?
            """,
            (host,)
        ).fetchone()[0]

        online = connection.execute(
            """
            SELECT COUNT(*)
            FROM network_logs
            WHERE host = ?
            AND status = 'ONLINE'
            """,
            (host,)
        ).fetchone()[0]

        offline = connection.execute(
            """
            SELECT COUNT(*)
            FROM network_logs
            WHERE host = ?
            AND status = 'OFFLINE'
            """,
            (host,)
        ).fetchone()[0]

        if total > 0:
            uptime = (online / total) * 100
            downtime = (offline / total) * 100
        else:
            uptime = 0
            downtime = 0

        statistics.append({
            "host": host,
            "uptime": uptime,
            "downtime": downtime
        })

    latency_data = []

    for host in HOSTS:

        rows = connection.execute(
            """
            SELECT host, timestamp, latency
            FROM network_logs
            WHERE host = ?
            AND latency IS NOT NULL
            AND latency != ''
            ORDER BY id DESC
            LIMIT 30
            """,
            (host,)
        ).fetchall()

        # Reverse so chart displays oldest -> newest
        rows = list(reversed(rows))

        for row in rows:

            latency_value = row["latency"]

            try:
                # Example: "29 ms" -> 29
                latency_value = float(
                    str(latency_value)
                    .replace("ms", "")
                    .strip()
                )

                latency_data.append({
                    "host": row["host"],
                    "timestamp": row["timestamp"],
                    "latency": latency_value
                })

            except (ValueError, TypeError):
                continue

    alerts = connection.execute(
        f"""
        SELECT *
        FROM network_logs
        WHERE host IN ({placeholders})
        AND event IN ('DOWN', 'RECOVERED')
        ORDER BY id DESC
        LIMIT 10
        """,
        HOSTS
    ).fetchall()

    connection.close()

    return render_template(
        "index.html",
        logs=logs,
        hosts=hosts,
        statistics=statistics,
        latency_data=latency_data,
        alerts=alerts,
        current_hosts=HOSTS
    )

if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    )