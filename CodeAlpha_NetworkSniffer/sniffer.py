from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

print("================================")
print(" Basic Network Sniffer Started ")
print("================================")

sniff(prn=packet_callback, count=20)

print("\nCapture Completed!")