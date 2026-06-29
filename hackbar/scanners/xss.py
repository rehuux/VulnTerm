#!/usr/bin/env python3

import urllib.parse
from ..core.colors import Fore, Style
from ..data.payloads import XSS_PAYLOADS

def scan_xss(app):
    """XSS Scanner"""
    app.print_cyan("\n[XSS Scanner]")
    app.print_white("=" * 40)
    
    url = app.get_url()
    param = app.get_param()
    base_url = f"{url}?{param}="
    
    app.print_yellow(f"[*] Target: {base_url}")
    app.print_yellow(f"[*] Testing {len(XSS_PAYLOADS)} payloads...")
    
    results = []
    
    for payload in XSS_PAYLOADS:
        result = _test_xss_payload(app, base_url, payload)
        if result:
            results.append(result)
            app.print_red(f"[!] VULNERABLE: {result}")
        else:
            app.print_green(f"[+] Safe: {payload[:30]}...")
    
    if results:
        app.print_red("\n[!] XSS vulnerability detected!")
    else:
        app.print_green("\n[+] No XSS vulnerability found.")
    
    report = f"XSS Scan Report\nTarget: {base_url}\n\n"
    report += "\n".join(results) if results else "No vulnerabilities found."
    app.save_report(report)
    return results

def _test_xss_payload(app, base_url, payload):
    test_url = base_url + urllib.parse.quote(payload)
    try:
        resp = app.session.get(test_url, timeout=app.timeout, proxies=app.proxy)
        if payload in resp.text:
            return f"Payload: {payload} | Reflected in response!"
        return None
    except:
        return None
