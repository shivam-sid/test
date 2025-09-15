# File: operations/hashing_core.py

import hashlib

def hash_md5(text: str) -> tuple[bool, str]:
    """Computes the MD5 hash of a string."""
    try:
        hash_object = hashlib.md5(text.encode('utf-8'))
        return True, hash_object.hexdigest()
    except Exception as e:
        return False, f"MD5 hashing failed: {e}"

def hash_sha1(text: str) -> tuple[bool, str]:
    """Computes the SHA-1 hash of a string."""
    try:
        hash_object = hashlib.sha1(text.encode('utf-8'))
        return True, hash_object.hexdigest()
    except Exception as e:
        return False, f"SHA-1 hashing failed: {e}"

def hash_sha256(text: str) -> tuple[bool, str]:
    """Computes the SHA-256 hash of a string."""
    try:
        hash_object = hashlib.sha256(text.encode('utf-8'))
        return True, hash_object.hexdigest()
    except Exception as e:
        return False, f"SHA-256 hashing failed: {e}"

def hash_sha512(text: str) -> tuple[bool, str]:
    """Computes the SHA-512 hash of a string."""
    try:
        hash_object = hashlib.sha512(text.encode('utf-8'))
        return True, hash_object.hexdigest()
    except Exception as e:
        return False, f"SHA-512 hashing failed: {e}"