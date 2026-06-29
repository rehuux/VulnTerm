#!/usr/bin/env python3

import hashlib
from ..core.colors import Fore, Style

def hash_decrypt(app):
    """Hash Decrypter"""
    app.print_cyan("\n[Hash Decrypter]")
    app.print_white("=" * 40)
    
    hash_input = app.get_input("Enter hash to decrypt")
    hash_type = _detect_hash_type(hash_input)
    app.print_cyan(f"[*] Detected hash type: {hash_type}")
    
    if hash_type == "Unknown":
        app.print_yellow("[!] Could not detect hash type. Trying MD5, SHA1, SHA256...")
    
    if hash_input in app.hash_db:
        app.print_green(f"\n[+] Found: {hash_input} -> {app.hash_db[hash_input]}")
        return app.hash_db[hash_input]
    
    result = _crack_hash(hash_input)
    if result:
        app.print_green(f"\n[+] Decrypted: {hash_input} -> {result}")
    else:
        app.print_yellow("\n[-] Could not decrypt. Try online tools.")
    return result

def _detect_hash_type(hash_input):
    length = len(hash_input)
    if length == 32:
        return "MD5"
    elif length == 40:
        return "SHA1"
    elif length == 64:
        return "SHA256"
    elif length == 96:
        return "SHA384"
    elif length == 128:
        return "SHA512"
    else:
        return "Unknown"

def _crack_hash(hash_input):
    common_words = [
        "password", "123456", "admin", "hello", "secret",
        "qwerty", "letmein", "monkey", "abc123", "dragon",
        "master", "sunshine", "princess", "iloveyou",
        "syedrehan", "rehuux", "hackbar", "terminal"
    ]
    
    for word in common_words:
        if hashlib.md5(word.encode()).hexdigest() == hash_input:
            return word
        if hashlib.sha1(word.encode()).hexdigest() == hash_input:
            return word
        if hashlib.sha256(word.encode()).hexdigest() == hash_input:
            return word
    return None
