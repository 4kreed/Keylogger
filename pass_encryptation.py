import os.path
from cryptography.fernet import Fernet

KEY_FILENAME = 'pass.key'
ENC_PASS_FILENAME = 'pass.enc'
PASSWORD = b'#######'

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILENAME, 'wb') as file:
        file.write(key)


def generate_encrypted_key(key):
    with open(ENC_PASS_FILENAME, 'wb') as file:
        fernet_key = Fernet(key)
        encrypted_password = fernet_key.encrypt(PASSWORD)
        file.write(encrypted_password)
        file.close()


def load_key():
    return open('pass.key', 'rb').read()


if __name__ == '__main__':

    generate_key()
    key = load_key()
    generate_encrypted_key(key)
