# yeh bas samjhne key liyeh hai ! 
#isko use mat krna apne code mai .
encode_dict = {
    'A': 'O', 'B': '9', 'C': '8', 'D': '7', 'E': '6', 'F': '5', 'G': 'Y', 'H': '3', 'I': '2', 'J': 'm', 'K': 'b', 'L': 'B',
    'M': 'V', 'N': 'c', 'O': 'x', 'P': 'Z', 'Q': 'k', 'R': 'K', 'S': 'J', 'T': 't', 'U': 'F', 'V': 'D', 'W': 'S', 'X': 'A',
    'Y': 'H', 'Z': 'R'
}

# Reverse the dictionary to decode the encoded message
decode_dict = {v: k for k, v in encode_dict.items()}

def encode_message(message):
    encoded_message = ''
    for char in message.upper():
        if char in encode_dict:
            encoded_message += encode_dict[char]
        else:
            encoded_message += char  # Keep any non-alphabet characters unchanged
    return encoded_message

def decode_message(message):
    decoded_message = ''
    for char in message:
        if char in decode_dict:
            decoded_message += decode_dict[char]
        else:
            decoded_message += char  # Keep any non-alphabet characters unchanged
    return decoded_message

# Main function puchega ki   encode hai decode
def main():
    print("Do you want to encode or decode a message?")
    choice = input("Type 'encode' to generate a code, or 'decode' to decode a code: ").lower()

    if choice == 'encode':
        message = input("Enter the message to encode: ")
        encoded = encode_message(message)
        print(f"Encoded message: {encoded}")
    elif choice == 'decode':
        message = input("Enter the encoded message to decode: ")
        decoded = decode_message(message)
        print(f"Decoded message: {decoded}")
    else:
        print("Invalid choice! Please type 'encode' or 'decode'.")

# Run the main function
if __name__ == "__main__":
    main()