import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def create_key(password):
        password = password.encode()
        kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=b'kb2rLgcp',
                iterations=100000,
                backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key

def encrypt(data, key):
        f = Fernet(key)
        encrypted = f.encrypt(data.encode())
        return encrypted.decode()

def decrypt(data, key):
        f = Fernet(key)
        decrypted = f.decrypt(data.encode())
        return decrypted.decode()
