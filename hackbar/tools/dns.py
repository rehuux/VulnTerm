#!/usr/bin/env python3

import socket
from ..core.colors import Fore, Style

def dns_lookup(app):
    """DNS Lookup"""
    app.print_cyan("\n[DNS Lookup]")
    app.print_white("=" * 40)
    
    host = app.get_input("Enter host/domain", "example.com")
    
    app.print_yellow(f"[*] Looking up {host}...")
    
    try:
        ips = socket.gethostbyname_ex(host)[2]
        app.print_cyan(f"[+] A Records:")
        for ip in ips:
            app.print_green(f"    - {ip}")
        
        for ip in ips:
            try:
                resolved = socket.gethostbyaddr(ip)[0]
                app.print_cyan(f"[+] Reverse: {ip} -> {resolved}")
            except:
                pass
        
        return ips
    except Exception as e:
        app.print_red(f"[!] Error: {e}")
        return None
