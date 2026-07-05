import pandas as pd


def analyze_packets():

    df = pd.read_csv("data/packets.csv")

    print("\n========== NETWORK TRAFFIC ANALYSIS ==========\n")

    # Total Packets
    print("Total Packets Captured :", len(df))

    # Protocol Count
    print("\nPackets by Protocol:\n")
    print(df["Protocol"].value_counts())

    # Top Source IP
    print("\nTop 5 Source IP Addresses:\n")
    print(df["Source IP"].value_counts().head())

    # Top Destination IP
    print("\nTop 5 Destination IP Addresses:\n")
    print(df["Destination IP"].value_counts().head())

    # Top Destination Ports
    print("\nTop 5 Destination Ports:\n")
    print(df["Destination Port"].value_counts().head())

    # Average Packet Size
    print("\nAverage Packet Size:")
    print(df["Packet Size"].mean(), "Bytes")