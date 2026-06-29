#!/usr/bin/env python3

import requests
import socket
import hashlib
import base64
import urllib.parse
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

from .colors import Fore, Style
from ..data.payloads import (
    SQLI_PAYLOADS, XSS_PAYLOADS, LFI_PAYLOADS,
    ADMIN_PATHS, COMMON_DIRS
)
from ..data.wordlists import HASH_DB, COMMON_PARAMS

class TerminalHackBar:
    """Main HackBar class"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        })
        self.timeout = 10
        self.max_threads = 10
        self.proxy = None
        self.hash_db = HASH_DB
    
    def print_red(self, text): print(f"{Fore.RED}{text}{Style.RESET_ALL}")
    def print_green(self, text): print(f"{Fore.GREEN}{text}{Style.RESET_ALL}")
    def print_yellow(self, text): print(f"{Fore.YELLOW}{text}{Style.RESET_ALL}")
    def print_blue(self, text): print(f"{Fore.BLUE}{text}{Style.RESET_ALL}")
    def print_cyan(self, text): print(f"{Fore.CYAN}{text}{Style.RESET_ALL}")
    def print_magenta(self, text): print(f"{Fore.MAGENTA}{text}{Style.RESET_ALL}")
    def print_white(self, text): print(f"{Fore.WHITE}{text}{Style.RESET_ALL}")
    
    def get_input(self, prompt, default=""):
        if default:
            result = input(f"{prompt} [{default}]: ").strip()
            return result if result else default
        return input(f"{prompt}: ").strip()
    
    def get_url(self):
        url = self.get_input("Enter target URL", "https://example.com")
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        return url.rstrip('/')
    
    def get_param(self):
        return self.get_input("Enter parameter name", "id")
    
    def save_report(self, data, filename=None):
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"hackbar_report_{timestamp}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Terminal HackBar Report\n")
            f.write(f"Author: Syed Rehan (@rehuux)\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("=" * 60 + "\n\n")
            f.write(data)
        
        self.print_green(f"[+] Report saved to: {filename}")
        return filename
    
    def show_menu(self):
        print(f"\n{Fore.CYAN}╔════════════════════════════════════════════╗")
        print(f"║  {Fore.WHITE}TERMINAL HACKBAR v2.0 - REHU{Fore.CYAN}         ║")
        print(f"╠════════════════════════════════════════════╣")
        print(f"║                                          ║")
        print(f"║  {Fore.YELLOW}[1]{Fore.WHITE} SQL Injection Scanner      {Fore.YELLOW}[8]{Fore.WHITE} Hash Decrypter")
        print(f"║  {Fore.YELLOW}[2]{Fore.WHITE} XSS Scanner               {Fore.YELLOW}[9]{Fore.WHITE} Encoder/Decoder")
        print(f"║  {Fore.YELLOW}[3]{Fore.WHITE} LFI/RFI Scanner           {Fore.YELLOW}[10]{Fore.WHITE} Directory Bruteforcer")
        print(f"║  {Fore.YELLOW}[4]{Fore.WHITE} Admin Panel Finder        {Fore.YELLOW}[11]{Fore.WHITE} HTTP Headers Check")
        print(f"║  {Fore.YELLOW}[5]{Fore.WHITE} Port Scanner              {Fore.YELLOW}[12]{Fore.WHITE} Parameter Fuzzer")
        print(f"║  {Fore.YELLOW}[6]{Fore.WHITE} DNS Lookup                {Fore.YELLOW}[13]{Fore.WHITE} WHOIS Lookup")
        print(f"║  {Fore.YELLOW}[7]{Fore.WHITE} All-in-One Scan           {Fore.YELLOW}[14]{Fore.WHITE} About")
        print(f"║                                          ║")
        print(f"║  {Fore.RED}[0]{Fore.WHITE} Exit{Fore.RED} (Press Ctrl+C anytime)             ║")
        print(f"╚════════════════════════════════════════════╝")
        return self.get_input("\nSelect option", "0")
    
    # Scanner methods
    def scan_sqli(self):
        from ..scanners.sqli import scan_sqli
        return scan_sqli(self)
    
    def scan_xss(self):
        from ..scanners.xss import scan_xss
        return scan_xss(self)
    
    def scan_lfi(self):
        from ..scanners.lfi import scan_lfi
        return scan_lfi(self)
    
    def find_admin(self):
        from ..scanners.admin import find_admin
        return find_admin(self)
    
    def scan_ports(self):
        from ..scanners.ports import scan_ports
        return scan_ports(self)
    
    def hash_decrypt(self):
        from ..tools.hash import hash_decrypt
        return hash_decrypt(self)
    
    def encode_decode(self):
        from ..tools.encode import encode_decode
        return encode_decode(self)
    
    def brute_dirs(self):
        from ..tools.dirs import brute_dirs
        return brute_dirs(self)
    
    def check_headers(self):
        from ..tools.headers import check_headers
        return check_headers(self)
    
    def fuzz_params(self):
        from ..tools.fuzz import fuzz_params
        return fuzz_params(self)
    
    def dns_lookup(self):
        from ..tools.dns import dns_lookup
        return dns_lookup(self)
    
    def whois_lookup(self):
        from ..tools.whois import whois_lookup
        return whois_lookup(self)
    
    def all_in_one(self):
        self.print_cyan("\n[All-in-One Scan]")
        self.print_white("=" * 40)
        self.scan_sqli()
        self.scan_xss()
        self.scan_lfi()
        self.find_admin()
        self.check_headers()
        self.print_green("\n[+] All-in-One scan completed!")
    
    def about(self):
        self.print_cyan("\n" + "=" * 50)
        self.print_white("  Terminal HackBar v2.0")
        self.print_white("  Advanced Security Testing Toolkit")
        self.print_white("")
        self.print_yellow("  Developed by: Syed Rehan (@rehuux)")
        self.print_yellow("  GitHub: https://github.com/rehuux")
        self.print_white("")
        self.print_white("  For Educational & Ethical Hacking Purposes Only")
        self.print_white("  Use only on systems you have permission to test")
        self.print_cyan("=" * 50)
    
    def run(self):
        while True:
            choice = self.show_menu()
            
            menu_actions = {
                "1": self.scan_sqli, "2": self.scan_xss,
                "3": self.scan_lfi, "4": self.find_admin,
                "5": self.scan_ports, "6": self.dns_lookup,
                "7": self.all_in_one, "8": self.hash_decrypt,
                "9": self.encode_decode, "10": self.brute_dirs,
                "11": self.check_headers, "12": self.fuzz_params,
                "13": self.whois_lookup, "14": self.about,
            }
            
            if choice == "0":
                self.print_green("\n[+] Goodbye! - Syed Rehan (@rehuux)")
                break
            
            if choice in menu_actions:
                try:
                    menu_actions[choice]()
                except KeyboardInterrupt:
                    self.print_yellow("\n[!] Operation cancelled")
                except Exception as e:
                    self.print_red(f"\n[!] Error: {e}")
            else:
                self.print_red("[!] Invalid option")
            
            input("\nPress Enter to continue...")
