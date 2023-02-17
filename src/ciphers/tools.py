# Text management tools
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

