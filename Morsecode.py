import pandas as pd # data processing CSV file
import tkinter as tk

# Read the CSV file into a pandas DataFrame
read = pd.read_csv('morse_code.csv')

# Ensure all Morse codes are strings and filter out non-string Morse codes
read['MorseCode'] = read['MorseCode'].astype(str)
MORSE_CODE_DICT = {char: code for char, code in zip(read['Character'],
                                                    read['MorseCode']) if isinstance(code, str)}

# Function to encrypt the string into Morse code
def encrypt(message):
    encrypted_message = ''
    for letter in message.upper():
        if letter in MORSE_CODE_DICT:
            encrypted_message += MORSE_CODE_DICT[letter] + ' '
        else:
            encrypted_message += letter
    return encrypted_message.strip()

# Function to decrypt the Morse code string into plain text
def decrypt(message):
    message += ' '
    deciphered_message = ''
    citext = ''
    for letter in message:
        if letter != ' ':
            i = 0
            citext += letter
        else:
            i += 1
            if i == 2:
                deciphered_message += ' '
            else:
                if citext in MORSE_CODE_DICT.values():
                    deciphered_message += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                else:
                    deciphered_message += 'Invalid Code'
                citext = ''
    return deciphered_message

# Create a UI application to execute the code
# Create the main application window
root = tk.Tk()
root.title("Morse Code")
root.geometry("500x650")
root.configure(bg="black")

# Title
title_label = tk.Label(root, text="Morse Code\n Encryption and Decryption ",
                       font=("Helvetica", 18, "bold"), fg="light gray", bg="black")
title_label.pack(pady=10)

# Encryption Section
encryption_label = tk.Label(root, text="Encryption", # title
                        font=("Helvetica", 14, "bold"), bg="black", fg="light gray")
encryption_label.pack(pady=7)

encrypt_note = tk.Label(root, text="Enter the message to Encrypt", # sub title
                        font=("Helvetica", 12), bg="black", fg="light gray")
encrypt_note.pack(pady=7)

# message input box
encrypt_entry = tk.Text(root, width=50, height=2)
encrypt_entry.pack(pady=7)

def on_encode():
    message = encrypt_entry.get("1.0", tk.END).strip()
    result = encrypt(message)
    encrypt_output.delete("1.0", tk.END)
    encrypt_output.insert(tk.END, result)

# Create a button to encode the message
encode_button = tk.Button(root, text="Encode", command=on_encode, width=10, font=("bold", 10))
encode_button.pack(pady=7)

# message output box
encrypt_output = tk.Text(root, width=50, height=2)
encrypt_output.pack(pady=7)

# Spacer to create space between encryption and decryption sections
spacer = tk.Label(root, text="", bg="black")
spacer.pack(pady=10)

# Decryption Section
decryption_label = tk.Label(root, text="Decryption",
                            font=("Helvetica", 14, "bold"), bg="black", fg="light gray")
decryption_label.pack(pady=7)

decrypt_note = tk.Label(root, text="Enter the Morse Code to Decrypt",
                        font=("Helvetica", 12), bg="black", fg="light gray")
decrypt_note.pack(pady=7)

# Morse code input box
decrypt_entry = tk.Text(root, width=50, height=2)
decrypt_entry.pack(pady=7)

def on_decode():
    message = decrypt_entry.get("1.0", tk.END).strip()
    result = decrypt(message)
    decrypt_output.delete("1.0", tk.END)
    decrypt_output.insert(tk.END, result)

# Create a button to decode the message
decode_button = tk.Button(root, text="Decode", command=on_decode, width=10, font=("bold", 10))
decode_button.pack(pady=7)

# Morse code output box
decrypt_output = tk.Text(root, width=50, height=2)
decrypt_output.pack(pady=7)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=root.quit, width=10, font=("bold", 10))
exit_button.pack(pady=30)

# Start the Tkinter main loop
root.mainloop()