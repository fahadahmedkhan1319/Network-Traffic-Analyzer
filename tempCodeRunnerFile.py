from packet_capture import start_sniffing
from analyzer import analyze_packets
from visualizer import create_graphs

print("=" * 40)
print("     NETWORK TRAFFIC ANALYZER")
print("=" * 40)

while True:

    print("\nPlease choose an option:\n")
    print("1. Capture Live Packets")
    print("2. Analyze Saved Packets")
    print("3. Generate Graphs")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ")

    if choice == "1":
        print("\nStarting Packet Capture...\n")
        start_sniffing()

    elif choice == "2":
        print("\nAnalyzing Captured Packets...\n")
        analyze_packets()

    elif choice == "3":
        print("\nGenerating Graphs...\n")
        create_graphs()

    elif choice == "4":
        print("\nThank you for using the Network Traffic Analyzer.")
        print("Exiting the program...")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 4.")