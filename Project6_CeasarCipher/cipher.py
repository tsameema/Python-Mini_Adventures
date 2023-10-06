class CaesarCipher():

  def generate_alphabets(self):
    """
      Generate the ASCII characters from letter 'A' to 'Z'

      RETURN:
        list : A list having alphabets only in upper letter
    """
    return [chr(i) for i in range(128) if 'A' <= chr(i) <= 'Z']

  def choice_to_encrypt_decrypt_msg(self):
    """
      User Input based function if he want to encrypt the message or decrypt it

      ARGS : None

      RETURN:
        is_de_encrypt (str) : if 'e' encrypt message else decrypt it if it is 'd'

    """
    while True:
      is_de_encrypt = input('Do you want to (e)ncrypt or (d)ecrypt? ').lower()
      if is_de_encrypt in ['e', 'd']:
        return is_de_encrypt
      else:
        print('Enter either "e" to encrypt message or "d" to decrypt message')
        continue

  def shift_keys(self, maxletters):
    """
      User input key to shift the letters that must lie with in range

      ARGS:
        maxletters (int) : length of alphabets generated

      RETURNS:
        key (int) :  shift alphabets by how much amount

    """
    while True:
      key = input(f'Please enter the key (0 to {maxletters}) to use. ')
      if key.isdigit() and 0 <= int(key) <= maxletters:
        return int(key)
      else:
        print(f'Enter integer key within range [1, {maxletters}]')
        continue

  def get_message(self, is_de_encrypt):
    """
      Get user input based prompt either to encrypt or decrypt.

      Args:
        is_de_encrypt (str): user desire to de/en-crypt message

      Returns:
        str : user message
    """
    return input('Enter the message to encrypt: ') if is_de_encrypt=='e' else  input('Enter the message to decrypt: ')

  def encrypt_decrypt_message(self, is_de_encrypt, message, ascii_letter, key):
    """
        Encrypt or decrypt a message using the Caesar Cipher algorithm.

        Args:
            is_encrypt (str): 'e' for encryption, 'd' for decryption.
            message (str): The message to be encrypted or decrypted.
            key (int): The encryption or decryption key.

        Returns:
            str: The encrypted or decrypted message.
    """
    crypt_msg = ''
    for idx, msg in enumerate(message):
      if msg.upper() in ascii_letter:
        msg_key = ascii_letter.index(msg.upper())

        if is_de_encrypt == 'e':
          n_idx = key + msg_key
          if n_idx > len(ascii_letter)-1:
            n_idx -= len(ascii_letter)
        elif is_de_encrypt == 'd':
          n_idx = key-msg_key
          if n_idx > 0:
            n_idx -= len(ascii_letter)

        crypt_msg +=  ascii_letter[abs(n_idx)]
      else:
        crypt_msg += msg
    return crypt_msg

  def generate_cipher(self):
    """
        Generate a Caesar Cipher for user-provided input.

        Args:
            None

        Returns:
            None
    """
    ascii_letter = self.generate_alphabets()
    is_de_encrypt  = self.choice_to_encrypt_decrypt_msg()
    key = self.shift_keys(len(ascii_letter)-1)
    message = self.get_message(is_de_encrypt)
    crypt_message = self.encrypt_decrypt_message(is_de_encrypt, message, ascii_letter, key)
    print('\nYOUR MESSAGE IN CAESAR CIPHER:')
    print(crypt_message)

if __name__ == '__main__':
  cipher = CaesarCipher()
  cipher.generate_cipher()


    



