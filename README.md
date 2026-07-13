# Network Traffic Analyzer Using Python

## Project Overview

The Network Traffic Analyzer is a Python-based application designed to capture, monitor, analyze, and visualize network traffic in real time. The application captures live packets from the network using the Scapy library, extracts important packet information, stores the captured data in CSV format, performs statistical analysis using the Pandas library, and generates graphical visualizations using Matplotlib.

The project demonstrates the practical implementation of packet sniffing, network traffic analysis, and data visualization techniques. It provides users with valuable insights into network communication while helping students understand the fundamentals of computer networking and packet analysis.

---

# Objectives

The objectives of this project are:

- Capture live network packets.
- Extract useful packet information.
- Store captured packet data in CSV format.
- Analyze captured network traffic.
- Generate graphical reports for visualization.
- Develop a simple and user-friendly network monitoring application.
- Enhance understanding of computer networking concepts.

---

# Key Features

- Live packet capturing using Scapy
- Real-time display of packet information
- Automatic storage of captured packets in CSV format
- Protocol-wise traffic analysis
- Source IP and Destination IP analysis
- Destination Port analysis
- Average packet size calculation
- Graph generation using Matplotlib
- Menu-driven command-line interface
- Modular and well-organized project structure

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Scapy | Live Packet Capture |
| Pandas | Data Analysis |
| Matplotlib | Graph Generation |
| CSV | Data Storage |
| Datetime Module | Timestamp Generation |
| OS Module | File and Directory Management |
| Visual Studio Code | Development Environment |
 | Wireshark | Packet Analysis and Traffic Verification |
 
 # Wireshark Integration

Wireshark was used during the testing phase to validate the packets captured by the Python-based Network Traffic Analyzer. It was used to inspect TCP, UDP, and DNS traffic and verify that the packet information matched the data captured by the application.

The primary packet capturing, analysis, CSV storage, and graph generation functionalities were implemented using Python, while Wireshark served only as a protocol verification and packet inspection tool.

---

# Project Structure

```text
Packet_Sniffer_Project/

|-- main.py
|-- packet_capture.py
|-- analyzer.py
|-- visualizer.py
|-- requirements.txt
|-- README.md

|-- data/
|   |-- packets.csv

graphs/
|-- protocol_distribution_bar.png
|-- protocol_distribution_pie.png
|-- top_source_ips.png
|-- top_destination_ports.png
|-- packet_size_distribution.png

|-- screenshots/
```

---

# System Workflow

```text
Start
   |
   V

Run main.py
   |
   V

Display Main Menu
   |
   +----------------------+----------------------+----------------------+
   |                      |                      |
   V                      V                      V

Capture Live        Analyze Saved          Generate
Packets             Packet Data            Graph

   |                      |                      |
   V                      V                      V

Save Packet Data    Read CSV File       Create Protocol
into packets.csv    Analyze Traffic     Distribution Graph

   |                      |                      |
   +----------------------+----------------------+
                          |
                          V

                         End
```

---

# Installation Guide

## Step 1

Install Python (Version 3.10 or later).

Download Python from:

https://www.python.org/downloads/

---

## Step 2

Download or Clone the Project.

Using Git:

```bash
git clone https://github.com/yourusername/network-traffic-analyzer.git
```

Or simply download the project ZIP file and extract it.

---

## Step 3

Open the project folder.

```bash
cd Packet_Sniffer_Project
```

---

## Step 4

Install the required Python libraries.

Using requirements.txt:

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install scapy pandas matplotlib
```

---

# Running the Application

Run the project using:

```bash
python main.py
```

The application displays the following menu:

```text
===================================
     NETWORK TRAFFIC ANALYZER
===================================

1. Capture Live Packets
2. Analyze Saved Packets
3. Generate Graph
4. Exit
Enter your choice (1-4):
```

---

# Application Modules

## 1. Packet Capture Module

This module captures live packets from the network using Scapy.

The following information is extracted for every packet:

- Time
- Source IP Address
- Destination IP Address
- Protocol
- Source Port
- Destination Port
- Packet Size

All captured packets are automatically stored in:

```text
data/packets.csv
```

---

## 2. Traffic Analysis Module

This module reads the captured packet data from the CSV file and performs statistical analysis.

The analysis includes:

- Total packets captured
- Protocol distribution
- Top Source IP Addresses
- Top Destination IP Addresses
- Most frequently used Destination Ports
- Average packet size

---

## 3. Graph Generation Module

The visualization module generates multiple graphical representations of the captured network traffic using Matplotlib.

It generates:

Protocol Distribution (Bar Chart)
Protocol Distribution (Pie Chart)
Top 5 Source IP Addresses
Top 5 Destination Ports
Packet Size Distribution

All graphs are automatically saved inside the graphs folder.
```

---

# Sample Packet Capture

```text
Time             : 2026-07-05 15:04:21
Source IP        : 192.168.0.121
Destination IP   : 142.250.202.142
Protocol         : TCP
Source Port      : 61705
Destination Port : 443
Packet Size      : 60 Bytes
```

---

# Sample Analysis Output

```text
========== NETWORK TRAFFIC ANALYSIS ==========

Total Packets Captured : 1992

Packets by Protocol

TCP    : 202
UDP    : 1790

Top Source IP Addresses

192.168.0.121
150.129.7.108

Top Destination Ports

443
5222

Average Packet Size

946.54 Bytes
```

---

# Generated Output

The application automatically generates the following files.

```text
data/

    packets.csv

graphs/

protocol_distribution_bar.png
protocol_distribution_pie.png
top_source_ips.png
top_destination_ports.png
packet_size_distribution.png
```

---

# Advantages

- Captures live network traffic.
- Simple and easy-to-use interface.
- Stores packet information automatically.
- Performs quick statistical analysis.
- Generates graphical reports.
- Modular and maintainable source code.
- Lightweight implementation suitable for educational purposes.

---

# Limitations

- Command-line interface only.
- Captures traffic from the selected network interface.
- Requires administrator privileges on certain operating systems.
- Does not inspect encrypted packet payloads.

---

# Future Enhancements

Future versions of this project may include:

- Graphical User Interface (GUI)
- Real-time network dashboard
- Advanced packet filtering
- Intrusion Detection System (IDS)
- IP geolocation
- PDF report generation
- Excel export
- Database integration
- Real-time alerts and notifications
- Network bandwidth monitoring

---

# Learning Outcomes

This project provides practical experience in:

- Computer Networking
- Packet Sniffing
- Network Traffic Analysis
- Python Programming
- Data Visualization
- Data Analysis
- File Handling
- Modular Programming
- Real-Time Network Monitoring

---

# Conclusion

The Network Traffic Analyzer successfully demonstrates the implementation of live packet capturing, network traffic analysis, and graphical visualization using Python. The application captures network packets, extracts useful information, stores the data in CSV format, performs statistical analysis, and generates protocol-based graphs. The project provides a practical understanding of packet-level communication and serves as an effective educational tool for learning network monitoring concepts.

---

## Project Screenshots

Store the following screenshots inside the **screenshots** folder for documentation purposes.

```text
screenshots/

01_project_files.png
02_main_menu.png
03_packet_capture.png
04_analysis_output.png
05_packets_csv.png
06_protocol_distribution_bar.png
07_protocol_distribution_pie.png
08_top_source_ips.png
09_top_destination_ports.png
10_packet_size_distribution.png
11_program_start.png
12_graph_generation.png
13_wireshark_capture.png
14_wireshark_tcp_capture.png
15_wireshark_udp.png
16_wireshark_dns.png
```

These screenshots document the complete workflow of the application, including project structure, packet capture, traffic analysis, graph generation, and Wireshark-based packet verification.

---

**End of Document**