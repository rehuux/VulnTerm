# VulnTerm Documentation

Welcome to the official documentation for **Terminal HackBar** — a powerful, terminal-based security auditing toolkit developed by **Syed Rehan (@rehuux)**.

---

## 📖 Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Available Tools](#available-tools)
5. [Examples](#examples)
6. [Reports](#reports)
7. [FAQ](#faq)
8. [Contributing](#contributing)
9. [License](#license)

---

## Introduction

VulnTerm is a CLI tool designed for **ethical hacking** and **penetration testing**. It brings the capabilities of a browser-based HackBar directly to your terminal.

### Key Features

- 🧩 **Comprehensive Scanning:** SQL Injection, XSS, LFI/RFI
- 🔎 **Reconnaissance:** Admin Panel Finder, Directory Bruteforcer
- 🛠️ **Utility Tools:** Hash Decrypter, Encoder/Decoder, DNS/WHOIS Lookup
- 🖥️ **User-Friendly CLI:** Color-coded, intuitive interface
- 📊 **Automated Reporting:** Detailed scan reports
- ⚡ **Multi-Threaded:** Fast concurrent scanning

### Disclaimer

> ⚠️ This tool is **for educational and ethical hacking purposes only**. Use only on systems you have permission to test. The author does not condone any illegal or malicious use.

---

## Installation

### Prerequisites

- Python 3.6 or higher
- `pip` (Python package manager)

### Steps

```bash
# Clone the repository
git clone https://github.com/rehuux/terminal-hackbar.git
cd terminal-hackbar

# Install dependencies
pip install -r requirements.txt

# Run the tool
python run.py
```

Install as Package

```bash
pip install -e .
hackbar
```

---

Usage

After launching the tool, you'll see the REHU banner and an interactive menu:

```text
╔════════════════════════════════════════════╗
║  TERMINAL HACKBAR v2.0 - REHU             ║
╠════════════════════════════════════════════╣
║  [1] SQL Injection Scanner    [8] Hash Decrypter
║  [2] XSS Scanner              [9] Encoder/Decoder
║  [3] LFI/RFI Scanner          [10] Directory Bruteforcer
║  [4] Admin Panel Finder       [11] HTTP Headers Check
║  [5] Port Scanner             [12] Parameter Fuzzer
║  [6] DNS Lookup               [13] WHOIS Lookup
║  [7] All-in-One Scan          [14] About
║  [0] Exit
╚════════════════════════════════════════════╝
```

Simply enter the number corresponding to the tool you want to use and follow the prompts.

---

Available Tools

1. SQL Injection Scanner

Detects SQL injection vulnerabilities by testing various payloads.

Usage: Enter URL and parameter name.

Example:

```bash
Enter target URL: https://example.com/page.php
Enter parameter name: id
```

2. XSS Scanner

Detects Cross-Site Scripting vulnerabilities.

Usage: Enter URL and parameter name.

3. LFI/RFI Scanner

Detects Local/Remote File Inclusion vulnerabilities.

Usage: Enter URL and parameter name.

4. Admin Panel Finder

Finds common admin panel paths.

Usage: Enter base URL.

5. Port Scanner

Scans open ports on a target host.

Usage: Enter host/IP and port range.

6. DNS Lookup

Performs DNS resolution and reverse lookup.

Usage: Enter domain name.

7. All-in-One Scan

Runs all scanners sequentially.

8. Hash Decrypter

Attempts to decrypt common hash types (MD5, SHA1, SHA256).

Usage: Enter hash string.

9. Encoder/Decoder

Encode/decode text in Base64, URL, Hex, or Binary.

10. Directory Bruteforcer

Finds common directories on a web server.

11. HTTP Headers Check

Displays HTTP headers and security header analysis.

12. Parameter Fuzzer

Tests common parameter names on a target URL.

13. WHOIS Lookup

Retrieves domain WHOIS information.

14. About

Shows tool information and credits.

---

Examples

SQL Injection Scan

```bash
Select option: 1
Enter target URL: https://example.com/page.php
Enter parameter name: id

[*] Target: https://example.com/page.php?id=
[*] Testing 36 payloads...
[!] VULNERABLE: Payload: ' OR '1'='1 | Status: 200
[!] VULNERABLE: Payload: ' UNION SELECT NULL-- | Status: 200
[+] Report saved to: hackbar_report_20250101_120000.txt
```

XSS Scan

```bash
Select option: 2
Enter target URL: https://example.com/search.php
Enter parameter name: q

[*] Target: https://example.com/search.php?q=
[!] VULNERABLE: Payload: <script>alert(1)</script> | Reflected in response!
[+] Report saved to: hackbar_report_20250101_120001.txt
```

---

Reports

All scan results are automatically saved to text files in the current directory.

Report Format:

```text
Terminal HackBar Report
Author: Syed Rehan (@rehuux)
Generated: 2025-01-01 12:00:00
============================================================

[Scan Results]
...
```

---

FAQ

Q: Is this tool legal?

A: Yes, when used on systems you own or have explicit permission to test. Unauthorized testing is illegal.

Q: Do I need an internet connection?

A: Yes, for scanning remote targets. Local scans (like port scanning) may not require internet.

Q: Can I use this on Windows?

A: Yes, it works on Windows, Linux, and macOS.

Q: What if colorama is not installed?

A: The tool includes a fallback to ANSI color codes.

Q: How do I stop a scan?

A: Press Ctrl+C at any time.

---

Contributing

We welcome contributions! Please read our Contributing Guide.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

Development Setup

```bash
git clone https://github.com/rehuux/terminal-hackbar.git
cd terminal-hackbar
pip install -e .
pip install pytest
python -m pytest tests/
```

---

License

Distributed under the MIT License. See LICENSE for more information.

---

Author

Syed Rehan (@rehuux)

· GitHub: @rehuux

---

Acknowledgements

· Built with Python and the open-source community.
· Inspired by various security testing tools.

---

Documentation maintained by Syed Rehan (@rehuux)

```

---

## 📁 Updated Structure

```

terminal-hackbar/
├── .github/
│   └── workflows/
│       └── python-package.yml
├── hackbar/
│   ├── init.py
│   ├── main.py
│   ├── core/
│   │   ├── init.py
│   │   ├── banner.py
│   │   ├── colors.py
│   │   └── base.py
│   ├── scanners/
│   │   ├── init.py
│   │   ├── sqli.py
│   │   ├── xss.py
│   │   ├── lfi.py
│   │   ├── admin.py
│   │   └── ports.py
│   ├── tools/
│   │   ├── init.py
│   │   ├── hash.py
│   │   ├── encode.py
│   │   ├── dirs.py
│   │   ├── headers.py
│   │   ├── fuzz.py
│   │   ├── dns.py
│   │   └── whois.py
│   └── data/
│       ├── init.py
│       ├── payloads.py
│       └── wordlists.py
├── tests/
│   ├── init.py
│   ├── test_sqli.py
│   ├── test_xss.py
│   └── test_utils.py
├── docs/
│   └── index.md
├── run.py
├── setup.py
├── requirements.txt
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── .gitignore

```
