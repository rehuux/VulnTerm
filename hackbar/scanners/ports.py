#!/usr/bin/env python3

import socket
from concurrent.futures import ThreadPoolExecutor, as_completed
from ..core.colors import Fore, Style

def scan_ports(app):
    """Port Scanner"""
    app.print_cyan("\n[Port Scanner]")
    app.print_white("=" * 40)
    
    host = app.get_input("Enter host/IP", "127.0.0.1")
    start_port = int(app.get_input("Start port", "1"))
    end_port = int(app.get_input("End port", "1024"))
    
    app.print_yellow(f"[*] Scanning {host} from port {start_port} to {end_port}")
    
    open_ports = []
    
    def scan_port(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            sock.close()
            if result == 0:
                return port
        except:
            pass
        return None
    
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(scan_port, port): port for port in range(start_port, end_port + 1)}
        
        for future in as_completed(futures):
            port = futures[future]
            try:
                result = future.result(timeout=2)
                if result:
                    open_ports.append(result)
                    app.print_green(f"[+] Port {result} is open")
            except:
                pass
    
    if open_ports:
        app.print_cyan(f"\n[+] Found {len(open_ports)} open ports:")
        service_map = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP",
            53: "DNS", 80: "HTTP", 110: "POP3", 111: "RPC",
            135: "MSRPC", 139: "NetBIOS", 143: "IMAP",
            443: "HTTPS", 445: "SMB", 993: "IMAPS",
            995: "POP3S", 3306: "MySQL", 5432: "PostgreSQL",
            27017: "MongoDB", 6379: "Redis", 8080: "HTTP-Alt"
        }
        for p in open_ports:
            if p in service_map:
                app.print_cyan(f"    - {p}: {service_map[p]}")
    else:
        app.print_yellow("\n[-] No open ports found.")
    
    report = f"Port Scan Report\nTarget: {host}\n\n"
    report += "\n".join([f"Port {p} open" for p in open_ports]) if open_ports else "No open ports found."
    app.save_report(report)
    return open_ports
