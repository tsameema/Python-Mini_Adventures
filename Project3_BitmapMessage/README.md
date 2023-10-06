# Bitmap Message Encoder

The Bitmap Message Encoder is a Python script that allows you to encode a message within a bitmap pattern by replacing designated characters in the bitmap with characters from the message. It provides a fun way to display messages in a visual format.
This program uses a multiline string as a
bitmap, a 2D image with only two possible
colors for each pixel, to determine how it
should display a message from the user. In this
bitmap, space characters represent an empty space,
and all other characters are replaced by characters in
the user’s message. The provided bitmap resembles
a world map, but you can change this to any image
you’d like. The binary simplicity of the space-ormessage-characters system makes it good for beginners. Try experimenting with different messages to
see what the results look like!

## Usage

1. Clone this repository to your local machine or download the Python script (`bitmap_message.py`).

2. Make sure you have Python installed on your system.

3. Run the script using the following command:

    python bitmap_message.py


## Methodology


1. A Python script, named bitmap_message.py, was created as the core of the project.
        - The script was organized into a class named BitmapMessage to encapsulate the functionality for generating the encoded message.
2. Functionality Development:

        - The BitmapMessage class was designed to have three main functions:
                - __init__: This constructor initializes the class with the bitmap pattern, message, and the character to be replaced in the bitmap.
                - generate_message: This function generates the coded message by processing the bitmap pattern and replacing designated characters with message characters.
                
                The generate_message function uses modular arithmetic to ensure that the message characters wrap around if the message is shorter than the bitmap.


## Example
1. An example of a bitmap pattern is given
2. You will be prompted to enter the message you want to display within the bitmap.
3. The script will generate a coded message by replacing specific characters in the provided bitmap pattern with the characters from your message.
4. The coded message will be displayed in the console.


## Customization
You can customize the bitmap pattern, the character to replace in the pattern, and the message to display by modifying the variables in the script.

bitmap: Replace this variable with your desired bitmap pattern.

replace_bitmap: Set this variable to the character you want to replace in the bitmap (default is '*').

message: Input your message when prompted.


