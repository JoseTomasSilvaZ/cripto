from scapy.all import IP, ICMP, sr1
from cesar import cesar



def send_ping():
    message = cesar()
    for character in message:
        packet = IP(dst="8.8.8.8", ttl=20)/ICMP()/(character)
        resp = sr1(packet, timeout=10)
        print(resp)

send_ping()