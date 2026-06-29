#!/usr/bin/env python3

import subprocess
import platform
from ..core.colors import Fore, Style

def whois_lookup(app):
    """WHOIS Lookup"""
    app.print_cyan("\n[WHOIS Lookup]")
    app.print_white("=" * 40)
    
    domain = app.get_input("Enter domain", "example.com")
    
    app.print_yellow(f"[*] Looking up {domain}...")
    
    try:
        if platform.system() == "Windows":
            app.print_yellow("[!] WHOIS not available on Windows by default.")
            app.print_yellow("[!] Try: https://who.is")
        else:
            result = subprocess.run(["whois", domain], capture_output=True, text=True, timeout=30)
            print(result.stdout[:2000])
            if len(result.stdout) > 2000:
                app.print_yellow(f"\n[!] Output truncated. Full output saved to report.")
            
            report = f"WHOIS Lookup Report\nDomain: {domain}\n\n"
            report += result.stdout
            app.save_report(report)
    except FileNotFoundError:
        app.print_yellow("[!] WHOIS command not found. Try: apt-get install whois (Linux) or brew install whois (Mac)")
    except Exception as e:
        app.print_red(f"[!] Error: {e}")
