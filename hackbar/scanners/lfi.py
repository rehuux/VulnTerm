#!/usr/bin/env python3

import urllib.parse
from ..core.colors import Fore, Style
from ..data.payloads import LFI_PAYLOADS

def scan_lfi(app):
    """LFI/RFI Scanner"""
    app.print_cyan("\n[LFI/RFI Scanner]")
    app.print_white("=" * 40)
    
    url = app.get_url()
    param = app.get_param()
    base_url = f"{url}?{param}="
    
    app.print_yellow(f"[*] Target: {base_url}")
    app.print_yellow(f"[*] Testing {len(LFI_PAYLOADS)} payloads...")
    
    found = []
    
    for payload in LFI_PAYLOADS:
        result = _test_lfi_payload(app, base_url, payload)
        if result:
            found.append(result)
            app.print_red(f"[!] LFI/RFI detected: {result}")
    
    if found:
        app.print_red("\n[!] LFI/RFI vulnerabilities found!")
    else:
        app.print_green("\n[+] No LFI/RFI vulnerability found.")
    
    report = f"LFI/RFI Scan Report\nTarget: {base_url}\n\n"
    report += "\n".join(found) if found else "No vulnerabilities found."
    app.save_report(report)
    return found

def _test_lfi_payload(app, base_url, payload):
    test_url = base_url + urllib.parse.quote(payload)
    try:
        resp = app.session.get(test_url, timeout=app.timeout, proxies=app.proxy)
        
        lfi_indicators = [
            "root:", "root:x:0:0", "daemon:", "bin:", "sys:",
            "win.ini", "[extensions]", "[mci extensions]",
            "hosts", "127.0.0.1", "localhost",
            "[boot loader]", "[operating systems]"
        ]
        
        text = resp.text.lower()
        for indicator in lfi_indicators:
            if indicator.lower() in text:
                return f"Payload: {payload} | Matched: {indicator} | Status: {resp.status_code}"
        return None
    except:
        return None
