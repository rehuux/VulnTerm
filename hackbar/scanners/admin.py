#!/usr/bin/env python3

from concurrent.futures import ThreadPoolExecutor, as_completed
from ..core.colors import Fore, Style
from ..data.payloads import ADMIN_PATHS

def find_admin(app):
    """Admin Panel Finder"""
    app.print_cyan("\n[Admin Panel Finder]")
    app.print_white("=" * 40)
    
    base_url = app.get_url()
    
    app.print_yellow(f"[*] Target: {base_url}")
    app.print_yellow(f"[*] Checking {len(ADMIN_PATHS)} paths...")
    
    found = []
    
    with ThreadPoolExecutor(max_workers=app.max_threads) as executor:
        futures = {executor.submit(_check_admin_path, app, base_url, path): path for path in ADMIN_PATHS}
        
        for future in as_completed(futures):
            path = futures[future]
            try:
                result = future.result(timeout=5)
                if result:
                    found.append(result)
                    app.print_green(f"[+] Found: {result}")
            except:
                pass
    
    if found:
        app.print_cyan(f"\n[+] Found {len(found)} admin panels:")
        for f in found:
            app.print_green(f"    - {f}")
    else:
        app.print_yellow("\n[-] No admin panels found.")
    
    report = f"Admin Panel Finder Report\nTarget: {base_url}\n\n"
    report += "\n".join(found) if found else "No admin panels found."
    app.save_report(report)
    return found

def _check_admin_path(app, base_url, path):
    test_url = f"{base_url.rstrip('/')}/{path}"
    try:
        resp = app.session.get(test_url, timeout=5, proxies=app.proxy, allow_redirects=False)
        if resp.status_code == 200:
            return test_url
        elif resp.status_code in [301, 302, 303, 307, 308]:
            return f"{test_url} -> {resp.headers.get('Location', '')[:50]}..."
        return None
    except:
        return None
