from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime
import csv
import os

# CSV file path
csv_file = "data/packets.csv"

# Create CSV file if it does not exist
if not os.path.exists(csv_file):
    with open(csv_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Time",
            "Source IP",
            "Destination IP",
            "Protocol",
            "Source Port",
            "Destination Port",
            "Packet Size"
        ])


def process_packet(packet):

    if IP in packet:

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        packet_size = len(packet)

        protocol = "Other"
        source_port = "-"
        destination_port = "-"

        if TCP in packet:
            protocol = "TCP"
            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport

        elif UDP in packet:
            protocol = "UDP"
            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport

        elif ICMP in packet:
            protocol = "ICMP"

        print("=" * 70)
        print("Time             :", current_time)
        print("Source IP        :", source_ip)
        print("Destination IP   :", destination_ip)
        print("Protocol         :", protocol)
        print("Source Port      :", source_port)
        print("Destination Port :", destination_port)
        print("Packet Size      :", packet_size, "Bytes")

        # Save packet to CSV
        with open(csv_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                current_time,
                source_ip,
                destination_ip,
                protocol,
                source_port,
                destination_port,
                packet_size
            ])


def start_sniffing():
    print("Packet Sniffer Started...\n")
    sniff(prn=process_packet, store=False)