import sys

def get_alpha_starting_point(char):
    return ord('A') if char.isupper() else ord('a')

def get_not_alpha_starting_point(char):
    return ord('0') if char.isdigit() else 32  

def compute_alpha_output(char, offset):
    start = get_alpha_starting_point(char)
    '''
    E.g -> with char = b and offset = 3
    start = 97
    ord = 98
    (98 - 97 + 3) % 26 = 4
    chr(97 + 4) = e
    '''
    return chr((ord(char) - start + offset) % 26 + start)

def compute_not_alpha_output(char, offset):
    if char.isdigit():
        start = ord('0')
        return chr((ord(char) - start + offset) % 10 + start)
    else:
        return chr((ord(char) + offset) % 128)

def caesar(message, offset):
    offset = int(offset)
    output = ""
    for char in message:
        if char.isalpha():
            output += compute_alpha_output(char, offset)
        elif char.isdigit() or (32 < ord(char) < 127): 
            output += compute_not_alpha_output(char, offset)
        else:
            output += char  

    return output

def main():
    if len(sys.argv) != 3:
        print(f"Usage: python3 {sys.argv[0]} <message> <offset>")
        sys.exit(1)
    
    message = sys.argv[1]
    offset = sys.argv[2]
    print(caesar(message, offset))

if __name__ == "__main__":
    main()
