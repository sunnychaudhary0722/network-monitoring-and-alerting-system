# Network Monitoring and Alerting System

A Python-based network monitoring and alerting system that continuously monitors configured hosts, measures network performance, detects status changes, stores monitoring data, and provides a web-based dashboard for visualization and analysis.

## Features

- Continuous network host monitoring
- ICMP ping-based availability checks
- Packet loss measurement
- Average latency measurement
- ONLINE / OFFLINE status detection
- DOWN and RECOVERED event detection
- Timestamped monitoring records
- CSV logging
- SQLite database storage
- Flask-based web dashboard
- Availability statistics
- Latency monitoring charts
- Alert history
- Monitoring logs
- Monitoring period filters
- Configurable monitoring hosts

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core monitoring and alerting logic |
| Flask | Web dashboard |
| SQLite | Monitoring data storage |
| HTML5 | Dashboard structure |
| CSS3 | Dashboard styling |
| JavaScript | Dashboard interactions |
| Chart.js | Latency visualization |
| ICMP Ping | Network availability testing |

## System Architecture

```text
                         +----------------------+
                         |   Configured Hosts   |
                         |                      |
                         | Router / DNS / Host  |
                         +----------+-----------+
                                    |
                                    v
                         +----------------------+
                         |    Python Monitor    |
                         |                      |
                         |  ICMP Ping Checks    |
                         |  Packet Loss        |
                         |  Latency             |
                         |  Status Detection    |
                         |  Event Detection     |
                         +----------+-----------+
                                    |
                     +--------------+--------------+
                     |                             |
                     v                             v
             +---------------+             +---------------+
             | SQLite        |             | CSV           |
             | Database      |             | Logs          |
             +-------+-------+             +---------------+
                     |
                     v
             +----------------------+
             |    Flask Dashboard   |
             |                      |
             | Current Host Status  |
             | Availability         |
             | Latency Charts       |
             | Alerts               |
             | Monitoring Logs       |
             | Time Filters          |
             +----------------------+
How It Works

The system follows a continuous monitoring workflow:

1. Configure Hosts

Hosts to monitor are defined in config.py.

HOSTS = [
    "192.168.1.1",
    "8.8.8.8",
    "1.1.1.1"
]

The list can be modified according to the monitoring requirements.

2. Send Ping Requests

monitor.py continuously sends ICMP ping requests to each configured host.

The system checks whether each host responds and measures its network performance.

3. Measure Network Performance

For each host, the system collects:

Packet loss
Average latency
Response status
Timestamp
4. Determine Host Status

Based on the ping results, the system determines whether a host is:

ONLINE

or

OFFLINE

A host can still be classified as ONLINE when at least one ping response is received, even if some packets are lost.

5. Detect Status Changes

The system tracks previous host states and detects important events:

INITIAL
DOWN
RECOVERED

For example:

ONLINE → OFFLINE = DOWN

OFFLINE → ONLINE = RECOVERED
6. Store Monitoring Data

Every monitoring check is recorded in:

SQLite database
CSV log file

The database stores information such as:

Timestamp
Host
Status
Packet Loss
Latency
Event
7. Display Results

The Flask dashboard reads the stored monitoring data and presents it through a web interface.

The dashboard provides:

Current host status
Availability statistics
Packet loss information
Latency monitoring
Recent alerts
Monitoring logs
Historical monitoring periods
Project Structure
network-monitoring-and-alerting-system/
│
├── dashboard/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── config.py
├── monitor.py
├── check_database.py
├── test_alert.py
├── requirements.txt
├── README.md
└── .gitignore
Installation
Clone the Repository
git clone https://github.com/sunnychaudhary0722/network-monitoring-and-alerting-system.git
Navigate to the Project
cd network-monitoring-and-alerting-system
Create a Virtual Environment
python -m venv venv
Activate the Virtual Environment

Windows PowerShell:

.\venv\Scripts\Activate.ps1
Install Dependencies
pip install -r requirements.txt
Running the Network Monitor

Start the monitoring system:

python monitor.py

The monitor will continuously check the configured hosts and record monitoring results.

Running the Dashboard

Open another terminal in the project directory and activate the virtual environment.

Then run:

python dashboard/app.py

Open the dashboard in a browser:

http://127.0.0.1:5000
Monitoring Metrics
Availability

Availability represents the percentage of monitoring checks during which a host was online.

Availability = (Online Checks / Total Checks) × 100
Packet Loss

Packet loss represents the percentage of ping packets that did not receive a response.

Packet Loss	Meaning
0%	All packets received
50%	Half of the packets lost
100%	No packets received
Latency

Latency represents the approximate round-trip time between the monitoring system and the monitored host.

Lower latency generally indicates faster network response.

Dashboard

The web dashboard provides a centralized view of the monitored network.

Current Host Status

Displays the latest status of each configured host:

ONLINE
OFFLINE
Availability Statistics

Displays uptime and downtime percentages for each monitored host.

Latency Monitoring

The dashboard visualizes latency measurements over time using Chart.js.

Alerts

The dashboard displays detected status-change events, including:

DOWN
RECOVERED
Monitoring Logs

Recent monitoring records are displayed with:

Timestamp
Host
Status
Packet loss
Latency
Event
Monitoring Periods

The dashboard supports different monitoring periods, including:

1 Hour
24 Hours
7 Days
All Time
Database

Monitoring data is stored locally using SQLite.

The database table contains:

Field	Description
ID	Unique monitoring record
Timestamp	Time of the monitoring check
Host	Monitored host
Status	ONLINE or OFFLINE
Packet Loss	Percentage of lost packets
Latency	Average response time
Event	INITIAL, DOWN, RECOVERED, or normal

Generated database and log files are excluded from Git using .gitignore.

Testing

The project includes scripts for checking database records and testing alert functionality.

Check Database
python check_database.py
Test Alert Functionality
python test_alert.py
Important Note About ICMP

A host reported as OFFLINE does not necessarily mean that the device or server is actually unavailable.

Some devices, servers, firewalls, and networks may block ICMP or ping requests.

Therefore, the monitoring result indicates whether the host responded to the ICMP requests sent by this system.

Use Cases

This system can be used for:

Local network monitoring
Server availability monitoring
Basic infrastructure monitoring
Network troubleshooting
Network performance observation
Learning network automation with Python
Demonstrating monitoring and alerting concepts
Future Improvements

Potential future improvements include:

Email notifications
Telegram or Slack alerts
CPU and memory monitoring
TCP port monitoring
HTTP endpoint monitoring
Historical uptime reports
Network health scoring
Dashboard authentication
REST API
Docker deployment
Cloud deployment
Network anomaly detection
Disclaimer

This project is intended for monitoring systems and devices that you own or are authorized to monitor.

Author

Sunny Chaudhary

B.Tech Computer Science & Engineering with Specialization in Information Technology
