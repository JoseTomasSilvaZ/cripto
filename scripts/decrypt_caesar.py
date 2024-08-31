import string
from collections import Counter
from termcolor import colored

def get_alpha_starting_point(char):
    return ord('A') if char.isupper() else ord('a')

def compute_alpha_output(char, offset):
    start = get_alpha_starting_point(char)
    return chr((ord(char) - start - offset) % 26 + start)

def decrypt_message(encrypted_message, offset):
    output = ""
    for char in encrypted_message:
        if char.isalpha():
            output += compute_alpha_output(char, offset)
        else:
            output += char  
    return output

def calculate_probability(text):
    frequencies = {
        'E': 13.68, 'A': 12.53, 'O': 8.68, 'S': 7.98, 'R': 6.87, 
        'N': 6.71, 'I': 6.25, 'D': 5.86, 'L': 5.24, 'C': 4.68, 
        'T': 4.63, 'U': 3.93, 'M': 3.15, 'P': 2.52, 'B': 1.42, 
        'G': 1.01, 'V': 0.90, 'Y': 0.90, 'Q': 0.88, 'H': 0.70, 
        'F': 0.69, 'Z': 0.52, 'J': 0.44, 'Ñ': 0.31, 'X': 0.22, 
        'K': 0.11, 'W': 0.04
    }
    text = text.upper()
    counter = Counter(text)
    total_chars = sum(counter[char] for char in string.ascii_uppercase)
    
    probability = 0
    for char, freq in frequencies.items():
        probability += (counter[char] / total_chars) * freq
    
    return probability

def generate_all_combinations(encrypted_message):
    combinations = []
    for offset in range(1, 26):
        decrypted_message = decrypt_message(encrypted_message, offset)
        probability = calculate_probability(decrypted_message)
        combinations.append((decrypted_message, probability, offset))
    return combinations



