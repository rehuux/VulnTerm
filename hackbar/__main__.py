#!/usr/bin/env python3

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hackbar.core.banner import print_banner
from hackbar.core.base import TerminalHackBar

def main():
    """Main entry point"""
    try:
        print_banner()
        app = TerminalHackBar()
        app.run()
    except KeyboardInterrupt:
        print("\n\n[!] Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n[!] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
