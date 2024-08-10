# MorseCode-Encryption-and-Decryption
This project is a simple yet powerful application for encrypting and decrypting Morse code. 
It is built using Python, Tkinter for the GUI, and pandas for handling the Morse code data stored in a CSV file. 
The application allows users to input text, which can be converted into Morse code, and vice versa.

# Features
Encrypt Text to Morse Code: Convert plain text into Morse code using an easy-to-use interface.
Decrypt Morse Code to Text: Convert Morse code back to plain text, making it easy to understand encoded messages.
CSV-based Morse Code Dictionary: The Morse code dictionary is loaded from a CSV file, making it easy to update or modify the Morse code mappings.
Simple and Intuitive GUI: Built with Tkinter, the application provides a user-friendly interface with a clear layout.

# Prepare the CSV File
Could you make sure that you have a morse_code.csv file with two columns: Character and MorseCode?

Example:
|-------------|-------------|
|  Character  |  	MorseCode |
|-------------|-------------|
|    A    	  |      .-     |
|-------------|-------------|
|     B	      |     -...    |
|-------------|-------------|
|     C       |    -.-.     |
|-------------|-------------|
|    ...      |	   ...      |
|-------------|-------------|

# Usage
1. Encryption:
> Enter the message you want to encrypt into the "Encryption" section.
> Click the "Encode" button to see the Morse code equivalent.

2. Decryption:
> Enter the Morse code you want to decrypt into the "Decryption" section.
> Click the "Decode" button to see the plain text equivalent.

3. Exit:
> Click the "Exit" button to close the application.

# Project Structure

morse-code-encryption-decryption

> ├── morse_code.csv ---------->  CSV file containing Morse code mappings
> ├── MorseCode.py   ---------->  Main application file
> └── README.md      ---------->  Project documentation (this file)


Contribution
Contributions are welcome! Please feel free to fork the repository and submit a pull request if you have any ideas, suggestions, or issues.
