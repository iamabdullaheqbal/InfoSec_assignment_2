import hashlib

def hash_password(password: str) -> str:
    """
    Hash password using SHA-256
    Args:
        password: Plain text password to hash
    Returns:
        Hexadecimal string representation of the hash
    """
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
