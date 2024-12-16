message = input("Enter your message: ")



def remove_spaces(message):
    newMessage = ""
    for char in message:
        if char == " ":
            continue
        newMessage += char
    return newMessage.lower()

def encrypt(message):
    newMessage = ""
    for char in message:
        numeric_code = ord(char)
        if numeric_code >= 97 and numeric_code <= 122:
            new_numeric_code = numeric_code + 2
            if new_numeric_code > 122:
                new_numeric_code = (new_numeric_code - 122) + 96
            newMessage += chr(new_numeric_code)
        else:
            newMessage += char
    return newMessage

def decrypt(message):
    decrypted_message = ""
    for char in message:
        numeric_code = ord(char)
        if numeric_code >= 97 and numeric_code <= 122:
            new_numeric_code = numeric_code - 2
            if new_numeric_code < 97:
                new_numeric_code = (new_numeric_code - 97) + 123
            decrypted_message += chr(new_numeric_code)
        else:
            decrypted_message += char
    return decrypted_message
            


encryption = encrypt(remove_spaces(message))
decryption = decrypt(encryption)

print(f"Encryption: {encryption}")
print(f"Decryption: {decryption}")