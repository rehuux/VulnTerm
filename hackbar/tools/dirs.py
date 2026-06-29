#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, as_completed
from ..core.colors import Fore, Style
from ..data.payloads import COMMON_DIRS

def brute_dirs(app):
    """Directory Bruteforcer"""
    app.print_cyan("\n[Directory Bruteforcer]")
    app.print_white("=" * 40)
    
    base_url = app.get_url()
    
    app.print_yellow(f"[*] Target: {base_url}")
    app.print_yellow(f"[*] Checking {len(COMMON_DIRS)} directories...")
    
    found = []
    
    with ThreadPoolExecutor(max_workers=app.max_threads) as executor:
        futures = {executor.submit(_check_dir, app, base_url, d): d for d in COMMON_DIRS}
        
        for future in as_completed(futures):
            d = futures[future]
            try:
                result = future.result(timeout=5)
                if result:
                    found.append(result)
                    app.print_green(f"[+] Found: {result}")
            except:
                pass
    
    if found:
        app.print_cyan(f"\n[+] Found {len(found)} directories:")
        for f in found:
            app.print_green(f"    - {f}")
    else:
        app.print_yellow("\n[-] No directories found.")
    
    report = f"Directory Bruteforce Report\nTarget: {base_url}\n\n"
    report += "\n".join(found) if found else "No directories found."
    app.save_report(report)
    return found

def _check_dir(app, base_url, directory):
    test_url = f"{base_url.rstrip('/')}/{directory}"
    try:
        resp = app.session.get(test_url, timeout=3, proxies=app.proxy, allow_redirects=False)
        if resp.status_code == 200:
            return test_url
        elif resp.status_code in [301, 302, 303, 307, 308]:
            return f"{test_url} -> {resp.headers.get('Location', '')[:50]}..."
        return None
    except:
        return None
