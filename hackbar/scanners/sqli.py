#!/usr/bin/env python3

import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..core.colors import Fore, Style
from ..data.payloads import SQLI_PAYLOADS

def scan_sqli(app):
    """SQL Injection Scanner"""
    app.print_cyan("\n[SQL Injection Scanner]")
    app.print_white("=" * 40)
    
    url = app.get_url()
    param = app.get_param()
    base_url = f"{url}?{param}="
    
    app.print_yellow(f"[*] Target: {base_url}")
    app.print_yellow(f"[*] Testing {len(SQLI_PAYLOADS)} payloads...")
    
    results = []
    vulnerable = False
    
    with ThreadPoolExecutor(max_workers=app.max_threads) as executor:
        futures = {}
        for payload in SQLI_PAYLOADS:
            future = executor.submit(_test_sqli_payload, app, base_url, payload)
            futures[future] = payload
        
        for future in as_completed(futures):
            payload = futures[future]
            try:
                result = future.result(timeout=app.timeout + 2)
                if result:
                    results.append(result)
                    app.print_red(f"[!] VULNERABLE: {result}")
                    vulnerable = True
                else:
                    app.print_green(f"[+] Safe: {payload[:30]}...")
            except Exception as e:
                app.print_yellow(f"[!] Error with {payload[:30]}...: {e}")
    
    if vulnerable:
        app.print_red("\n[!] SQL Injection vulnerability detected!")
    else:
        app.print_green("\n[+] No SQL Injection vulnerability found.")
    
    report = f"SQL Injection Scan Report\nTarget: {base_url}\n\n"
    report += "\n".join(results) if results else "No vulnerabilities found."
    app.save_report(report)
    return results

def _test_sqli_payload(app, base_url, payload):
    test_url = base_url + urllib.parse.quote(payload)
    try:
        resp = app.session.get(test_url, timeout=app.timeout, proxies=app.proxy)
        
        sql_errors = [
            "sql", "mysql", "syntax error", "unclosed quotation",
            "you have an error", "warning: mysql", "odbc", "driver",
            "dbdriver", "database error", "sqlite", "postgresql",
            "ora-", "pls-", "jdbc", "exception", "stack trace",
            "division by zero", "column not found", "table not found"
        ]
        
        text = resp.text.lower()
        for error in sql_errors:
            if error in text:
                return f"Payload: {payload} | Error: {error} | Status: {resp.status_code}"
        
        if "sleep(5)" in payload.lower():
            if resp.elapsed.total_seconds() > 4:
                return f"Payload: {payload} | Time-based injection! ({resp.elapsed.total_seconds():.2f}s)"
        
        return None
    except:
        return None
