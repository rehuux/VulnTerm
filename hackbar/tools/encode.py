#!/usr/bin/env python3

import base64
import urllib.parse
from ..core.colors import Fore, Style

def encode_decode(app):
    """Encoder/Decoder Tool"""
    app.print_cyan("\n[Encoder/Decoder]")
    app.print_white("=" * 40)
    
    text = app.get_input("Enter text to encode/decode")
    
    print(f"\n{Fore.YELLOW}Choose operation:")
    print("  1. Base64 Encode")
    print("  2. Base64 Decode")
    print("  3. URL Encode")
    print("  4. URL Decode")
    print("  5. Hex Encode")
    print("  6. Hex Decode")
    print("  7. Binary Encode")
    print("  8. Binary Decode")
    print("  9. All Encodings")
    
    choice = app.get_input("Select operation", "1")
    
    if choice == "1":
        result = base64.b64encode(text.encode()).decode()
        app.print_green(f"\n[+] Base64 Encoded: {result}")
    elif choice == "2":
        try:
            result = base64.b64decode(text).decode()
            app.print_green(f"\n[+] Base64 Decoded: {result}")
        except:
            app.print_red("\n[!] Invalid Base64 string")
    elif choice == "3":
        result = urllib.parse.quote(text)
        app.print_green(f"\n[+] URL Encoded: {result}")
    elif choice == "4":
        result = urllib.parse.unquote(text)
        app.print_green(f"\n[+] URL Decoded: {result}")
    elif choice == "5":
        result = text.encode().hex()
        app.print_green(f"\n[+] Hex Encoded: {result}")
    elif choice == "6":
        try:
            result = bytes.fromhex(text).decode()
            app.print_green(f"\n[+] Hex Decoded: {result}")
        except:
            app.print_red("\n[!] Invalid Hex string")
    elif choice == "7":
        result = ' '.join(format(ord(c), '08b') for c in text)
        app.print_green(f"\n[+] Binary Encoded: {result}")
    elif choice == "8":
        try:
            result = ''.join(chr(int(x, 2)) for x in text.split())
            app.print_green(f"\n[+] Binary Decoded: {result}")
        except:
            app.print_red("\n[!] Invalid Binary string")
    elif choice == "9":
        _show_all_encodings(app, text)

def _show_all_encodings(app, text):
    print(f"\n{Fore.CYAN}Original: {text}")
    print(f"{Fore.GREEN}Base64: {base64.b64encode(text.encode()).decode()}")
    print(f"{Fore.GREEN}URL: {urllib.parse.quote(text)}")
    print(f"{Fore.GREEN}Hex: {text.encode().hex()}")
    print(f"{Fore.GREEN}Binary: {' '.join(format(ord(c), '08b') for c in text)}")
