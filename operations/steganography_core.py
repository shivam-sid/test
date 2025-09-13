# File: operations/steganography_core.py

import os
import base64
import numpy as np
from collections import deque
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken

# --- Constants ---
ENCRYPTION_ITERATIONS = 100000
MESSAGE_DELIMITER = "####"


def generate_key(password, salt=None):
    """Generates a key from a password using PBKDF2."""
    if salt is None:
        salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ENCRYPTION_ITERATIONS,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode())), salt


def encrypt_message(message, password):
    """Derives a key and encrypts the message using Fernet (AES-128-CBC)."""
    key, salt = generate_key(password)
    cipher = Fernet(key)
    # Prepend the salt to the encrypted message for later use in decryption
    return base64.b64encode(salt + cipher.encrypt(message.encode())).decode()


def decrypt_message(encrypted_data, password):
    """Derives the key using the salt and decrypts the message."""
    try:
        decoded_data = base64.b64decode(encrypted_data.encode())
        salt, encrypted_msg = decoded_data[:16], decoded_data[16:]
        key, _ = generate_key(password, salt)
        cipher = Fernet(key)
        return cipher.decrypt(encrypted_msg).decode()
    except InvalidToken:
        return "INVALID_PASSWORD"  # Special code for incorrect password
    except Exception:
        return None  # General failure


def encode_lsb(image_array, data):
    """Hides data within the least significant bits of an image."""
    data += MESSAGE_DELIMITER
    binary_data = ''.join(format(ord(c), '08b') for c in data)

    flat_img = image_array.flatten()
    if len(binary_data) > len(flat_img):
        return None  # Not enough space in the image

    binary_array = np.array(list(binary_data), dtype=np.uint8)

    # Modify the LSB of each pixel value
    flat_img[:len(binary_array)] = (flat_img[:len(binary_array)] & 0b11111110) | binary_array

    return flat_img.reshape(image_array.shape)


def decode_lsb(image_array):
    """Extracts data hidden in the least significant bits of an image."""
    flat_img = image_array.flatten()
    extracted_bits, byte_chars = [], []
    history = deque(maxlen=len(MESSAGE_DELIMITER))

    for pixel in flat_img:
        extracted_bits.append(pixel & 1)

        if len(extracted_bits) == 8:
            byte = int("".join(map(str, extracted_bits)), 2)
            char = chr(byte)
            byte_chars.append(char)
            history.append(char)
            extracted_bits = []

            # Check if we've found the end of the message
            if "".join(history) == MESSAGE_DELIMITER:
                return "".join(byte_chars[:-len(MESSAGE_DELIMITER)])

    return None  # Delimiter not found