# Caesar Cipher Hacker
This program can hack messages encrypted
with the Caesar cipher from Project 6, even
if you don’t know the key. There are only 26
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call this technique a brute-force attack. This program helps users find the original message by trying all possible shift keys.

## Methods
The CaesarHack class defines several methods to facilitate the decryption process:

#### generate_alphabets(): 
Generates a list of uppercase English letters from 'A' to 'Z'.

#### shift_keys(maxletters): 
Takes user input to determine the number of keys to try for decryption.

### get_message(): 
Takes user input for the encrypted Caesar cipher message.

### decrypt_message(message, ascii_letter, key):
Decrypts the message using the Caesar Cipher algorithm and displays the decrypted messages for all possible keys.

### generate_cipher():
Coordinates the decryption process by calling the above methods and taking user inputs.

## Example
Here's an example of how to use the Caesar Cipher Hacker program:

1. Run the program:  python caesar_hack.py
2. Enter the number of keys to try (0 to 25).
3. Enter the encrypted Caesar cipher message you want to decrypt.
4. The program will display the decrypted message for each possible key, allowing you to choose the correct decryption.
5. Once you've identified the correct key, you will see the decrypted message.
6. You can repeat the process with different messages or keys as needed.

Enter the number of keys to try (0 to 25).

> 6

Enter the encrypted Caesar cipher message to hack.

> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.

Key #0: QIIX QI FC XLI VSWI FYWLIW XSRMKLX.

Key #1: PHHW PH EB WKH URVH EXVKHV WRQLJKW.

Key #2: OGGV OG DA VJG TQUG DWUJGU VQPKIJV.

Key #3: NFFU NF CZ UIF SPTF CVTIFT UPOJHIU.

Key #4: MEET ME BY THE ROSE BUSHES TONIGHT.

Key #5: LDDS LD AX SGD QNRD ATRGDR SNMHFGS.

Key #6: KCCR KC ZW RFC PMQC ZSQFCQ RMLGEFR.


That's it! The Caesar Cipher Hacker helps you decrypt messages encrypted using the Caesar Cipher algorithm.

Feel free to customize and extend this program as needed for your specific use case.




