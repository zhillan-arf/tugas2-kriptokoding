# Text management tools
import pathlib

def group_to_fives(text):
    # Group text into five chars each. Groups separated by space
    grouped_chars = ""
    for i in range(0, len(text)):
        if text[i].isalpha():
            if (i % 5 == 0 and i != 0):
                grouped_chars += " "
            grouped_chars += text[i]
    return grouped_chars

def exten_group_to_fives(text):
    grouped_chars = ""
    for i in range(0, len(text)):
        if (i % 5 == 0 and i != 0):
            grouped_chars += " "
        grouped_chars += text[i]
    return grouped_chars

def no_space(text):
    return text.replace(" ", "")

def read_file(filename):
    # Read a txt file and turn it into string
    with open(filename, "r") as file:
        contents = file.read()
    return contents


def save_text_to_file(text, filename):
    # Save ciphertext into a file
    with open(filename, "w") as file:
        file.write(text)


def read_encrypt(filename):
    with open(filename, 'rb') as file:
        contents = file.read().decode('latin1')
    return contents


def export_encrypted(content, filename):
    with open(filename, 'wb') as file:
        file.write(content.encode('latin1'))


def export_decrypted(content, filename):
    with open(filename, 'wb') as file:
        file.write(content.encode('latin1'))


def write_binary(filename, contents):
    with open(filename, 'wb') as file:
        for char in contents:
            file.write(ord(char).to_bytes(1, 'big'))


def cleanse(text):
    # Throw all non-alphabet letters and capitalize it
    cleantext = ""
    for c in text:
        if c.isalpha():
            cleantext += c.upper()
    return cleantext


def secure_pos(pos):
    if pos == "":
        pos = "A"
    elif len(pos) > 1:
        pos = pos[0]
    return pos