import subprocess
import re
import time
import csv
import os
import sqlite3
from datetime import datetime

from config import HOSTS

hosts = HOSTS

previous_status = {}

statistics = {}

for host in hosts:
    statistics[host] = {
        "checks": 0,
        "online": 0,
        "offline": 0
    }

csv_file = "network_log.csv"

if not os.path.exists(csv_file):

    with open(csv_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Timestamp",
            "Host",
            "Status",
            "Packet Loss",
            "Latency",
            "Event"
        ])

db_file = "network_monitor.db"

connection = sqlite3.connect(db_file)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS network_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    host TEXT,
    status TEXT,
    packet_loss TEXT,
    latency TEXT,
    event TEXT
)
""")

connection.commit()

connection.close()


while True:

    print("\n" + "=" * 80)
    print("                    NETWORK MONITOR")
    print("=" * 80)

    current_time = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    print(f"Check Time: {current_time}")

    print("-" * 80)

    print(
        f"{'HOST':<20}"
        f"{'STATUS':<15}"
        f"{'LOSS':<12}"
        f"{'LATENCY':<12}"
        f"{'EVENT':<15}"
    )

    print("-" * 80)


    for host in hosts:



        result = subprocess.run(
            [
                r"C:\Windows\System32\PING.EXE",
                "-n",
                "4",
                "-w",
                "2000",
                host
            ],
            capture_output=True,
            text=True
        )

        output = result.stdout

        if result.returncode == 0:

            status = "ONLINE"

        else:

            status = "OFFLINE"

        loss_match = re.search(
            r"\((\d+)% loss\)",
            output
        )

        if loss_match:

            packet_loss = loss_match.group(1) + "%"

        else:

            packet_loss = "N/A"

        latency_match = re.search(
            r"Average = (\d+)ms",
            output
        )

        if latency_match:

            average_latency = (
                latency_match.group(1) + " ms"
            )

        else:

            average_latency = "N/A"


        if host not in previous_status:

            event = "INITIAL"


        elif (
            previous_status[host] == "ONLINE"
            and status == "OFFLINE"
        ):

            event = "DOWN"


        elif (
            previous_status[host] == "OFFLINE"
            and status == "ONLINE"
        ):

            event = "RECOVERED"


        else:

            event = "-"


        if event == "DOWN":

            print()
            print(
                f"🚨 ALERT: {host} is OFFLINE!"
            )


        elif event == "RECOVERED":

            print()
            print(
                f"✅ ALERT: {host} has RECOVERED!"
            )


        statistics[host]["checks"] += 1

        if status == "ONLINE":

            statistics[host]["online"] += 1

        else:

            statistics[host]["offline"] += 1


        print(
            f"{host:<20}"
            f"{status:<15}"
            f"{packet_loss:<12}"
            f"{average_latency:<12}"
            f"{event:<15}"
        )

        previous_status[host] = status

        with open(
            csv_file,
            "a",
            newline=""
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                current_time,
                host,
                status,
                packet_loss,
                average_latency,
                event
            ])


        connection = sqlite3.connect(db_file)

        cursor = connection.cursor()

        cursor.execute("""
        INSERT INTO network_logs
        (
            timestamp,
            host,
            status,
            packet_loss,
            latency,
            event
        )
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            current_time,
            host,
            status,
            packet_loss,
            average_latency,
            event
        ))

        connection.commit()

        connection.close()


    print("\n" + "=" * 80)
    print("                    AVAILABILITY")
    print("=" * 80)

    print(
        f"{'HOST':<20}"
        f"{'CHECKS':<10}"
        f"{'ONLINE':<10}"
        f"{'OFFLINE':<10}"
        f"{'UPTIME':<12}"
        f"{'DOWNTIME':<12}"
    )

    print("-" * 80)


    for host in hosts:

        checks = statistics[host]["checks"]

        online = statistics[host]["online"]

        offline = statistics[host]["offline"]


        if checks > 0:

            uptime = (
                online / checks
            ) * 100

            downtime = (
                offline / checks
            ) * 100

        else:

            uptime = 0

            downtime = 0


        print(
            f"{host:<20}"
            f"{checks:<10}"
            f"{online:<10}"
            f"{offline:<10}"
            f"{uptime:<10.2f}%"
            f"{downtime:<10.2f}%"
        )


    print("=" * 80)

    print("Next check in 5 seconds...")

    time.sleep(5)