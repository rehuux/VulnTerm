#!/usr/bin/env python3

from .colors import Fore, Style, init_colors

def print_banner():
    """Print the HackBar banner with REHU ASCII art"""
    init_colors()
    
    banner = f"""
{Fore.RED}  ██████{Fore.YELLOW}  ███████{Fore.RED}  ██   ██{Fore.YELLOW}  ██    ██                     
{Fore.RED}  ██   ██{Fore.YELLOW} ██   ██{Fore.RED} ██   ██{Fore.YELLOW}  ██    ██                     
{Fore.RED}  ██████{Fore.YELLOW}  ███████{Fore.RED}  ███████{Fore.YELLOW}  ██    ██                     
{Fore.RED}  ██   ██{Fore.YELLOW} ██   ██{Fore.RED} ██   ██{Fore.YELLOW}  ██    ██                     
{Fore.RED}  ██   ██{Fore.YELLOW} ██   ██{Fore.RED} ██   ██{Fore.YELLOW}  ███████                     

{Fore.CYAN}  ╔══════════════════════════════════════════════════════════════════╗
{Fore.CYAN}  ║                                                                  ║
{Fore.CYAN}  ║  {Fore.WHITE}Rehu HackBar v2.0 - Advanced Security Testing Suite{Fore.CYAN}    ║
{Fore.CYAN}  ║  {Fore.YELLOW}Developed by: {Fore.WHITE}Syed Rehan{Fore.CYAN}                                      ║
{Fore.CYAN}  ║  {Fore.YELLOW}GitHub: {Fore.WHITE}@rehuux{Fore.CYAN}                                        ║
{Fore.CYAN}  ║                                                                  ║
{Fore.CYAN}  ║  {Fore.RED}For Educational & Ethical Hacking Purposes Only{Fore.CYAN}                       ║
{Fore.CYAN}  ║  {Fore.RED}Use only on systems you have permission to test{Fore.CYAN}                       ║
{Fore.CYAN}  ╚══════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
"""
    print(banner)
