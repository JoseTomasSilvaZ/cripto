from scapy.all import rdpcap, IP, Raw, ICMP
from decrypt_caesar import generate_all_combinations
from termcolor import colored

def get_message(packet):
    if packet.haslayer(Raw):
        return chr(packet[Raw].load[8:][0])
    return ''  

def main():
    file = input("Enter the capture name (just name, not extension): ")
    packets = rdpcap(f"../ws_captures/{file}.pcapng")
    message = ''
    for packet in packets:
        if packet.haslayer(IP) and packet[IP].dst == '8.8.8.8':
            letter = get_message(packet)
            if letter:
                message += letter
    
    combinations = generate_all_combinations(message)
    best_combination = max(combinations, key=lambda x: x[1])
    for message, prob, offset in combinations:
        if message == best_combination[0]:
            print(colored(f"Offset {offset}: {message} (Prob: {prob:.2f})", 'green'))
        else:
            print(f"Offset {offset}: {message} (Prob: {prob:.2f})")

if __name__ == "__main__":
    main()