# File: operations/ciphers.py

def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> tuple[bool, str]:
    """
    Encrypts or decrypts text using the Caesar cipher method.

    Args:
        text (str): The input string to be processed.
        shift (int): The number of positions to shift letters.
        decrypt (bool): If True, the function will decrypt the text.
                         If False, it will encrypt.

    Returns:
        A tuple containing a boolean for success and the resulting string.
    """
    if not isinstance(shift, int):
        return False, "Shift value must be an integer."

    if decrypt:
        shift = -shift

    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            # Handle lowercase letters
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            result += shifted_char
        elif 'A' <= char <= 'Z':
            # Handle uppercase letters
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            result += shifted_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char

    return True, result


def atbash_cipher(text: str) -> tuple[bool, str]:
    """
    Encrypts or decrypts text using the Atbash cipher method.
    The cipher is reciprocal, so encryption and decryption are the same.
    """
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord('z') - ord(char) + ord('a'))
        elif 'A' <= char <= 'Z':
            result += chr(ord('Z') - ord(char) + ord('A'))
        else:
            result += char
    return True, result


def rot13_cipher(text: str) -> tuple[bool, str]:
    """
    Encrypts/decrypts text using the ROT13 cipher.
    ROT13 is a special case of the Caesar cipher with a shift of 13.
    """
    return caesar_cipher(text, 13)


def vigenere_cipher(text: str, key: str, decrypt: bool = False) -> tuple[bool, str]:
    """
    Encrypts/decrypts text using the Vigenère cipher.

    Args:
        text (str): The input string to be processed.
        key (str): The keyword to use for shifting.
        decrypt (bool): If True, the function will decrypt the text.

    Returns:
        A tuple containing a boolean for success and the resulting string.
    """
    if not key.isalpha():
        return False, "Key must contain only alphabetic characters."

    key_repeated = (key.upper() * (len(text) // len(key) + 1))[:len(text)]
    result = ""
    key_index = 0

    for char in text:
        shift = 0
        if 'a' <= char <= 'z':
            shift = ord(key_repeated[key_index]) - ord('A')
            if decrypt:
                shifted_char = chr(((ord(char) - ord('a') - shift + 26) % 26) + ord('a'))
            else:
                shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            result += shifted_char
            key_index += 1
        elif 'A' <= char <= 'Z':
            shift = ord(key_repeated[key_index]) - ord('A')
            if decrypt:
                shifted_char = chr(((ord(char) - ord('A') - shift + 26) % 26) + ord('A'))
            else:
                shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            result += shifted_char
            key_index += 1
        else:
            result += char

    return True, result


# File: operations/ciphers.py

# ... (existing functions)

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
import hashlib


def aes_encrypt(text: str, key: str) -> tuple[bool, str]:
    """Encrypts text using AES-256."""
    try:
        if len(key) not in [16, 24, 32]:
            return False, "Invalid AES key size. Must be 16, 24, or 32 bytes."

        key_bytes = key.encode('utf-8')
        iv = os.urandom(16)
        
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(text.encode('utf-8')) + padder.finalize()
        
        cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ct = encryptor.update(padded_data) + encryptor.finalize()
        
        return True, iv.hex() + ct.hex()
    except Exception as e:
        return False, f"Failed to encrypt with AES: {e}"


# File: operations/ciphers.py

# ... (rest of the file)

def des_encrypt(text: str, key: str) -> tuple[bool, str]:
    """Encrypts text using DES."""
    try:
        if len(key) != 8:
            return False, "Invalid DES key size. Must be 8 bytes."

        key_bytes = key.encode('utf-8')
        iv = os.urandom(8)
        
        padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
        padded_data = padder.update(text.encode('utf-8')) + padder.finalize()
        
        cipher = Cipher(algorithms.TripleDES(key_bytes), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ct = encryptor.update(padded_data) + encryptor.finalize()

        return True, iv.hex() + ct.hex()
    except Exception as e:
        return False, f"Failed to encrypt with DES: {e}"


def triple_des_encrypt(text: str, key: str) -> tuple[bool, str]:
    """Encrypts text using Triple DES."""
    try:
        # TDES keys must be 16 or 24 bytes
        if len(key) not in [16, 24]:
            return False, "Invalid Triple DES key size. Must be 16 or 24 bytes."
            
        key_bytes = key.encode('utf-8')
        iv = os.urandom(8)

        padder = padding.PKCS7(algorithms.TripleDES.block_size).padder()
        padded_data = padder.update(text.encode('utf-8')) + padder.finalize()

        cipher = Cipher(algorithms.TripleDES(key_bytes), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ct = encryptor.update(padded_data) + encryptor.finalize()
        
        return True, iv.hex() + ct.hex()
    except Exception as e:
        return False, f"Failed to encrypt with Triple DES: {e}"


def blowfish_encrypt(text: str, key: str) -> tuple[bool, str]:
    """Encrypts text using Blowfish."""
    try:
        # Blowfish key size must be between 4 and 56 bytes.
        if not 4 <= len(key) <= 56:
            return False, "Invalid Blowfish key size. Must be between 4 and 56 bytes."
            
        key_bytes = key.encode('utf-8')
        iv = os.urandom(8)

        padder = padding.PKCS7(algorithms.Blowfish.block_size).padder()
        padded_data = padder.update(text.encode('utf-8')) + padder.finalize()

        cipher = Cipher(algorithms.Blowfish(key_bytes), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ct = encryptor.update(padded_data) + encryptor.finalize()
        
        return True, iv.hex() + ct.hex()
    except Exception as e:
        return False, f"Failed to encrypt with Blowfish: {e}"
    

# File: operations/ciphers.py

# ... (existing functions)

def aes_decrypt(text: str, key: str) -> tuple[bool, str]:
    """Decrypts text using AES-256."""
    try:
        iv_hex = text[:32]
        ct_hex = text[32:]
        iv = bytes.fromhex(iv_hex)
        ct = bytes.fromhex(ct_hex)
        key_bytes = key.encode('utf-8')

        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        cipher = Cipher(algorithms.AES(key_bytes), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        
        padded_data = decryptor.update(ct) + decryptor.finalize()
        unpadded_data = unpadder.update(padded_data) + unpadder.finalize()
        
        return True, unpadded_data.decode('utf-8')
    except Exception as e:
        return False, f"Failed to decrypt with AES: {e}"


def des_decrypt(text: str, key: str) -> tuple[bool, str]:
    """Decrypts text using DES."""
    try:
        iv_hex = text[:16]
        ct_hex = text[16:]
        iv = bytes.fromhex(iv_hex)
        ct = bytes.fromhex(ct_hex)
        key_bytes = key.encode('utf-8')

        unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
        cipher = Cipher(algorithms.TripleDES(key_bytes), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        
        padded_data = decryptor.update(ct) + decryptor.finalize()
        unpadded_data = unpadder.update(padded_data) + unpadder.finalize()
        
        return True, unpadded_data.decode('utf-8')
    except Exception as e:
        return False, f"Failed to decrypt with DES: {e}"


def triple_des_decrypt(text: str, key: str) -> tuple[bool, str]:
    """Decrypts text using Triple DES."""
    try:
        iv_hex = text[:16]
        ct_hex = text[16:]
        iv = bytes.fromhex(iv_hex)
        ct = bytes.fromhex(ct_hex)
        key_bytes = key.encode('utf-8')

        unpadder = padding.PKCS7(algorithms.TripleDES.block_size).unpadder()
        cipher = Cipher(algorithms.TripleDES(key_bytes), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        
        padded_data = decryptor.update(ct) + decryptor.finalize()
        unpadded_data = unpadder.update(padded_data) + unpadder.finalize()
        
        return True, unpadded_data.decode('utf-8')
    except Exception as e:
        return False, f"Failed to decrypt with Triple DES: {e}"


def blowfish_decrypt(text: str, key: str) -> tuple[bool, str]:
    """Decrypts text using Blowfish."""
    try:
        iv_hex = text[:16]
        ct_hex = text[16:]
        iv = bytes.fromhex(iv_hex)
        ct = bytes.fromhex(ct_hex)
        key_bytes = key.encode('utf-8')

        unpadder = padding.PKCS7(algorithms.Blowfish.block_size).unpadder()
        cipher = Cipher(algorithms.Blowfish(key_bytes), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        
        padded_data = decryptor.update(ct) + decryptor.finalize()
        unpadded_data = unpadder.update(padded_data) + unpadder.finalize()
        
        return True, unpadded_data.decode('utf-8')
    except Exception as e:
        return False, f"Failed to decrypt with Blowfish: {e}"
    