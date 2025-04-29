from cryptography.fernet import Fernet

SECRET_KEY = b'BEfvwLZBsqvRF7RC_-q9Hw9u1QmtPBy2Zvk3VAi_ShY='

cipher_suite = Fernet(SECRET_KEY)

def encrypt_message(message: str) -> bytes:
    return cipher_suite.encrypt(message.encode())

def decrypt_message(encrypted_message: bytes) -> str:
    return cipher_suite.decrypt(encrypted_message).decode()
