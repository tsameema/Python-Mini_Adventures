# Caesar Cipher
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It
encrypts letters by shifting them over by a
certain number of places in the alphabet. We
call the length of shift the key. For example, if the
key is 3, then A becomes D, B becomes E, C becomes
F, and so on. To decrypt the message, you must shift
the encrypted letters in the opposite direction. This
program lets the user encrypt and decrypt messages
according to this algorithm.This Python class, CaesarCipher, provides a set of methods to perform Caesar Cipher encryption and decryption on user-provided messages.

## Usage
To use the CaesarCipher class, follow these steps:

1. Import the CaesarCipher class from the provided Python file.
2. Create an instance of the CaesarCipher class.
3. Call the generate_cipher method to perform encryption or decryption.

            from cipher import CaesarCipher
            cipher = CaesarCipher()
            cipher.generate_cipher()
## Methods
### generate_alphabets()
Generate a list of uppercase ASCII letters from 'A' to 'Z'.

**Parameters :** None

**Returns :** list: A list containing uppercase alphabets.
### choice_to_encrypt_decrypt_msg()
Prompt the user to choose whether they want to encrypt or decrypt a message.

**Parameters :** None

**Returns :** str: 'e' for encryption, 'd' for decryption.
### shift_keys(maxletters)
Prompt the user to enter a shift key for the Caesar Cipher.

**Parameters :** maxletters (int) :: The maximum number of letters in the alphabet (e.g., 26 for the English alphabet).

**Returns :** int :: The user-provided shift key.
### get_message(is_de_encrypt)
Prompt the user to enter a message for encryption or decryption.

**Parameters :** is_de_encrypt (str) :: 'e' for encryption, 'd' for decryption.

**Returns :** str :: The user-provided message.
### encrypt_decrypt_message(is_de_encrypt, message, ascii_letter, key)
Encrypt or decrypt a message using the Caesar Cipher algorithm.

**Parameters :** is_de_encrypt (str) :: 'e' for encryption, 'd' for decryption.

message (str) :: The message to be encrypted or decrypted.
           
ascii_letter (list) :: A list of uppercase ASCII letters.
             
key (int) :: The encryption or decryption key.

**Returns :** str :: The encrypted or decrypted message.
### generate_cipher()
Generate a Caesar Cipher for a user-provided message.

**Parameters :** None

**Returns :** None

## Example
Here's an example of how to use the CaesarCipher class:

        from cipher import CaesarCipher
        cipher = CaesarCipher()
        cipher.generate_cipher()
1. ENCRYPTED MESSAGE

**Do you want to (e)ncrypt or (d)ecrypt?**

> e

**Please enter the key (0 to 25) to use.**

> 4

**Enter the message to encrypt.**

> Meet me by the rose bushes tonight.

encrypted msg : QIIX QI FC XLI VSWI FYWLIW XSRMKLX.

2. DECRYPTED MESSAGE
   
**Do you want to (e)ncrypt or (d)ecrypt?**

> d

**Please enter the key (0 to 25) to use.**

> 4

**Enter the message to decrypt.**

> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.

decrypted msg : MEET ME BY THE ROSE BUSHES TONIGHT.

Follow the prompts to choose encryption or decryption, provide a shift key, and enter the message. The class will then display the encrypted or decrypted message in the Caesar Cipher.

Feel free to use and modify this CaesarCipher class in your Python projects for basic encryption and decryption tasks.
