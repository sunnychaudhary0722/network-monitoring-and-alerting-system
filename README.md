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
