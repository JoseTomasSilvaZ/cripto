def get_alpha_starting_point(char):
    return ord('A') if char.isupper() else ord('a')

def get_not_alpha_starting_point(char):
    return ord('0') if char.isdigit() else 32  

def compute_alpha_output(char, offset):
    start = get_alpha_starting_point(char)
    return chr((ord(char) - start + offset) % 26 + start)

def compute_not_alpha_output(char, offset):
    if char.isdigit():
        start = ord('0')
        return chr((ord(char) - start + offset) % 10 + start)
    else:
        return chr((ord(char) + offset) % 128)

def cesar(message, offset):
    output = ""
    for char in message:
        if char.isalpha():
            output += compute_alpha_output(char, offset)
        elif char.isdigit() or (32 < ord(char) < 127): 
            output += compute_not_alpha_output(char, offset)
        else:
            output += char  

    print("Mensaje cifrado:", output)

def main():
    message = input("Enter the message: ")
    offset = int(input("Enter the offset: "))
    cesar(message, offset)

if __name__ == "__main__":
    main()
