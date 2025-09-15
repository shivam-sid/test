# File: operations/asymmetric_ciphers.py

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import base64

def rsa_key_gen() -> tuple[bool, str]:
    """Generates a public and private RSA key pair."""
    try:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        return True, f"-----BEGIN PUBLIC KEY-----\n{public_pem.decode()}\n-----END PUBLIC KEY-----\n\n-----BEGIN PRIVATE KEY-----\n{private_pem.decode()}\n-----END PRIVATE KEY-----"
    except Exception as e:
        return False, f"Failed to generate RSA key pair: {e}"

def rsa_encrypt(text: str, public_key_pem: str) -> tuple[bool, str]:
    """Encrypts text using an RSA public key."""
    try:
        public_key = serialization.load_pem_public_key(
            public_key_pem.encode(),
            backend=default_backend()
        )

        ciphertext = public_key.encrypt(
            text.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return True, base64.b64encode(ciphertext).decode('utf-8')
    except Exception as e:
        return False, f"Failed to encrypt with RSA: {e}"

def rsa_decrypt(text: str, private_key_pem: str) -> tuple[bool, str]:
    """Decrypts text using an RSA private key."""
    try:
        private_key = serialization.load_pem_private_key(
            private_key_pem.encode(),
            password=None,
            backend=default_backend()
        )
        
        plaintext = private_key.decrypt(
            base64.b64decode(text.encode('utf-8')),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return True, plaintext.decode('utf-8')
    except Exception as e:
        return False, f"Failed to decrypt with RSA: {e}"