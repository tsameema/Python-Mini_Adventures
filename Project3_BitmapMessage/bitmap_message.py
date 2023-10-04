class BitmapMessage():

  def __init__(self, bitmap, message, replace_bitmap):
    """
    Initializes a BitmapMessage object.

    ARGS:
    - bitmap (str): The bitmap pattern to use.
    - message (str): The message to be displayed within the bitmap.
    - replace_bitmap (str): The character in the bitmap to be replaced with the message characters.

    RETURN: None
    """
    self.bitmap = bitmap
    self.message = message
    self.replace_bitmap = replace_bitmap

  def generate_message(self):
    """
    Generates a coded message by replacing characters in the bitmap with characters from the message.

    RETURN: str, the coded message.
    """
    bitmap_pattern = ""
    i=0
    for bitmap_lines in self.bitmap.splitlines():
      for bitmap_char in bitmap_lines:
        if bitmap_char ==' ':
          bitmap_pattern += bitmap_char
        elif bitmap_char == self.replace_bitmap:
          bitmap_pattern += self.message[i % len(message)]
          i += 1
      bitmap_pattern += '\n'
    return bitmap_pattern

if __name__ == "__main__":
  bitmap = """
  ....................................................................
    **************   *  *** **  *      ******************************
    ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
            *************          **  * **** ** ************** *
            *********            *******   **************** * *
              ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                      *****             ****              *********
                      ****              **                 *******   *
                      ***                                       *    *
                      **     *                    *
  ...................................................................."""

  message = input('Enter the message to display with the bitmap : ')
  replace_bitmap = '*'
  bitmap_msg = BitmapMessage(bitmap, message, replace_bitmap)
  coded_msg = bitmap_msg.generate_message()
  print(coded_msg)