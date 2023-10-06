class CaesarHack():

  def generate_alphabets(self):
    """
      Generate the ASCII characters from letter 'A' to 'Z'

      RETURN:
        list : A list having alphabets only in upper letter
    """
    return [chr(i) for i in range(128) if 'A' <= chr(i) <= 'Z']

  def shift_keys(self, maxletters):
    """
      User input key to try number of keys

      ARGS:
        maxletters (int) : length of alphabets generated

      RETURNS:
        key (int) :  number of shifting

    """
    while True:
      key = input(f'Please enter the key (0 to {maxletters}) to use.  ')
      if key.isdigit() and 0 <= int(key) <= maxletters:
        return int(key)
      else:
        print(f'Enter integer key within range [1, {maxletters}]')
        continue

  def get_message(self):
    """
      Get user input based prompt to decrypt

      Args:
        None

      Returns:
        str : user message
    """
    return input('Enter Encrypted Caesar cipher message to hack : ')

  def decrypt_message(self, message, ascii_letter, key):
    """
        Decrypt a message using the Caesar Cipher algorithm.

        Args:
            message (str): The message to be encrypted or decrypted.
            key (int): The encryption or decryption key.

        Returns:
            str: The decrypted message.
    """
    print('\nDECRYPTED MESSAGES : ')
    try_key = 0
    while try_key <= key:
      crypt_msg = ''
      for idx, msg in enumerate(message):
        if msg.upper() in ascii_letter:
          msg_key = ascii_letter.index(msg.upper())
          n_idx = try_key-msg_key
          if n_idx > 0:
            n_idx -= len(ascii_letter)
          crypt_msg +=  ascii_letter[abs(n_idx)]
        else:
          crypt_msg += msg
      print(f'Key #{try_key} : {crypt_msg}')
      try_key += 1

  def generate_cipher(self):
    """
        Generate a Caesar Cipher for user-provided input.

        Args:
            None

        Returns:
            None
    """
    ascii_letter = self.generate_alphabets()
    key = self.shift_keys(len(ascii_letter))
    message = self.get_message()
    self.decrypt_message(message, ascii_letter, key)

if __name__ == '__main__':
  cipher = CaesarHack()
  cipher.generate_cipher()


    





