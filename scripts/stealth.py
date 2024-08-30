from scapy.all import IP, ICMP, sr1, Raw
import sys 
import time
import struct

def generate_timestamp():
    ts = int(time.time()) & 0xFFFFFFFF
    return struct.pack("<Q",ts)

def generate_packet(destination, timestamp, number, payload):
    return IP(dst=destination)/ICMP(type=8, id=1, seq=number)/bytes(timestamp)/Raw(load=payload)

def generate_icmp_payload():
    payload = b""
    for i in range(0x10, 0x38):
        payload+= bytes([i])
    return payload

def send_packet(packet):
    sr1(packet)

def send_letter(destination, letter, number):
    payload = letter.encode()
    payload += b"\x00" * 7
    payload += generate_icmp_payload() 
    print(generate_timestamp())
    packet = generate_packet(destination, generate_timestamp(), number, payload)
    send_packet(packet)
    
def send_packets(message):
    for i in range(len(message)):
        send_letter("8.8.8.8", message[i], i+1)   

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <encrypted_message>")
        sys.exit(1)
    send_packets(sys.argv[1])

