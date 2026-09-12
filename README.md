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

<img width="2856" height="1438" alt="Screenshot 2026-09-12 183133" src="https://github.com/user-attachments/assets/4791e977-3989-43e9-98e8-792b8d55ad96" />
<img width="2816" height="1528" alt="Screenshot 2026-09-12 183156" src="https://github.com/user-attachments/assets/29fd42a0-12af-47c7-b907-a1270628399f" />
<img width="2694" height="1012" alt="Screenshot 2026-09-12 183212" src="https://github.com/user-attachments/assets/21d80e10-17f9-431c-83e0-26c8c2943304" />
<img width="2682" height="1226" alt="Screenshot 2026-09-12 183221" src="https://github.com/user-attachments/assets/6cc2d0f0-4a33-4e67-bdaa-604ad4086f6d" />




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
                         |  Packet Loss         |
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
             | Monitoring Logs      |
             | Time Filters         |
             +----------------------+
