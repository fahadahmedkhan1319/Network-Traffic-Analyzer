import pandas as pd
import matplotlib.pyplot as plt
import os


def create_graphs():

    # Read CSV file
    df = pd.read_csv("data/packets.csv")

    # Create graphs folder if it doesn't exist
    os.makedirs("graphs", exist_ok=True)

    # ------------------------------------------
    # Graph 1 : Protocol Distribution (Bar Chart)
    # ------------------------------------------

    protocol_counts = df["Protocol"].value_counts()

    plt.figure(figsize=(8,5))
    protocol_counts.plot(kind="bar")
    plt.title("Protocol Distribution (Bar Chart)")
    plt.xlabel("Protocol")
    plt.ylabel("Packet Count")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.savefig("graphs/protocol_distribution_bar.png")
    plt.close()

    # ------------------------------------------
    # Graph 2 : Protocol Distribution (Pie Chart)
    # ------------------------------------------

    plt.figure(figsize=(7,7))
    protocol_counts.plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90
    )

    plt.ylabel("")
    plt.title("Protocol Distribution (Pie Chart)")
    plt.tight_layout()
    plt.savefig("graphs/protocol_distribution_pie.png")
    plt.close()

    # ------------------------------------------
    # Graph 3 : Top 5 Source IP Addresses
    # ------------------------------------------

    top_ips = df["Source IP"].value_counts().head(5)

    plt.figure(figsize=(8,5))
    top_ips.plot(kind="barh")

    plt.title("Top 5 Source IP Addresses")
    plt.xlabel("Packet Count")
    plt.ylabel("Source IP")
    plt.tight_layout()

    plt.savefig("graphs/top_source_ips.png")
    plt.close()

    # ------------------------------------------
    # Graph 4 : Top 5 Destination Ports
    # ------------------------------------------

    top_ports = df["Destination Port"].value_counts().head(5)

    plt.figure(figsize=(8,5))
    top_ports.plot(kind="barh")

    plt.title("Top 5 Destination Ports")
    plt.xlabel("Packet Count")
    plt.ylabel("Destination Port")
    plt.tight_layout()

    plt.savefig("graphs/top_destination_ports.png")
    plt.close()

    # ------------------------------------------
    # Graph 5 : Packet Size Distribution
    # ------------------------------------------

    plt.figure(figsize=(8,5))
    df["Packet Size"].plot(kind="hist", bins=20)

    plt.title("Packet Size Distribution")
    plt.xlabel("Packet Size (Bytes)")
    plt.ylabel("Frequency")
    plt.tight_layout()

    plt.savefig("graphs/packet_size_distribution.png")
    plt.close()

    print("\n===================================")
    print(" All graphs generated successfully!")
    print("===================================\n")

    print("Saved graphs:")

    print("- protocol_distribution_bar.png")
    print("- protocol_distribution_pie.png")
    print("- top_source_ips.png")
    print("- top_destination_ports.png")
    print("- packet_size_distribution.png")