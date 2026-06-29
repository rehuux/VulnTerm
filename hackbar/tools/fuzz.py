#!/usr/bin/env python3

from ..core.colors import Fore, Style
from ..data.wordlists import COMMON_PARAMS

def fuzz_params(app):
    """Parameter Fuzzer"""
    app.print_cyan("\n[Parameter Fuzzer]")
    app.print_white("=" * 40)
    
    url = app.get_url()
    
    app.print_yellow(f"[*] Target: {url}")
    app.print_yellow(f"[*] Testing {len(COMMON_PARAMS)} parameters...")
    
    found = []
    
    for param in COMMON_PARAMS:
        test_url = f"{url}?{param}=test"
        try:
            resp = app.session.get(test_url, timeout=3, proxies=app.proxy)
            if resp.status_code == 200:
                if "test" in resp.text:
                    found.append(param)
                    app.print_green(f"[+] Parameter accepted: {param}")
        except:
            pass
    
    if found:
        app.print_cyan(f"\n[+] Found {len(found)} working parameters:")
        for f in found:
            app.print_green(f"    - {f}")
    else:
        app.print_yellow("\n[-] No parameters accepted.")
    
    return found
