#!/usr/bin/env python3

from ..core.colors import Fore, Style

def check_headers(app):
    """HTTP Headers Checker"""
    app.print_cyan("\n[HTTP Headers Checker]")
    app.print_white("=" * 40)
    
    url = app.get_url()
    
    app.print_yellow(f"[*] Target: {url}")
    
    try:
        resp = app.session.get(url, timeout=app.timeout, proxies=app.proxy)
        
        app.print_cyan("\n[+] Headers:")
        print(f"    {Fore.WHITE}Status: {Fore.GREEN}{resp.status_code} {resp.reason}")
        print(f"    {Fore.WHITE}Server: {Fore.CYAN}{resp.headers.get('Server', 'Unknown')}")
        print(f"    {Fore.WHITE}Content-Type: {Fore.CYAN}{resp.headers.get('Content-Type', 'Unknown')}")
        print(f"    {Fore.WHITE}Content-Length: {Fore.CYAN}{resp.headers.get('Content-Length', 'Unknown')}")
        print(f"    {Fore.WHITE}Date: {Fore.CYAN}{resp.headers.get('Date', 'Unknown')}")
        print(f"    {Fore.WHITE}X-Powered-By: {Fore.CYAN}{resp.headers.get('X-Powered-By', 'Unknown')}")
        
        app.print_cyan("\n[+] Security Headers:")
        sec_headers = {
            'X-Frame-Options': 'Clickjacking protection',
            'X-Content-Type-Options': 'MIME sniffing protection',
            'X-XSS-Protection': 'XSS protection',
            'Strict-Transport-Security': 'HSTS',
            'Content-Security-Policy': 'CSP',
            'Referrer-Policy': 'Referrer policy',
        }
        
        for header, desc in sec_headers.items():
            if header in resp.headers:
                app.print_green(f"    [+] {header}: {resp.headers[header]} ({desc})")
            else:
                app.print_red(f"    [-] {header} (Missing - {desc})")
        
        return resp.headers
    except Exception as e:
        app.print_red(f"[!] Error: {e}")
        return None
