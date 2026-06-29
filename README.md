# VulnTerm

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

> **A terminal-based security auditing toolkit for ethical hacking and penetration testing.**

VulnTerm is a powerful, all-in-one CLI tool designed for security professionals and ethical hackers. It brings the capabilities of a browser-based HackBar directly to your terminal, allowing you to perform comprehensive security assessments, including SQL injection, XSS, and LFI/RFI scanning, all from a single, unified command-line interface.

---

## ✨ Features

*   **🧩 Comprehensive Scanning:** Perform SQL Injection, XSS, and LFI/RFI vulnerability scans.
*   **🔎 Reconnaissance:** Find admin panels, brute-force directories, and discover working parameters.
*   **🛠️ Utility Tools:** Decrypt hashes, encode/decode data, and perform DNS/WHOIS lookups.
*   **🖥️ User-Friendly CLI:** Color-coded, intuitive terminal interface designed for efficiency.
*   **📊 Automated Reporting:** Generate detailed reports of all scan results.
*   **⚡ Multi-Threaded:** Lightning-fast scanning with support for concurrent operations.

---

## 🚀 Quick Start

### Prerequisites

*   Python 3.6 or higher
*   `pip` (Python package manager)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/rehuux/vulnterm.git
    cd vulnterm
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the tool:**
    ```bash
    python run.py
    ```
    Or, after installing in development mode:
    ```bash
    pip install -e .
    vulnterm
    ```

---

## 💻 Usage

After launching the tool, you'll be presented with an interactive menu:

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

Simply enter the number corresponding to the tool you wish to use and follow the on-screen prompts.

Example: SQL Injection Scan

```bash
Select option: 1
Enter target URL: https://example.com/page.php
Enter parameter name: id
[*] Target: https://example.com/page.php?id=
[*] Testing 36 payloads...
[+] VULNERABLE: Payload: ' OR '1'='1 | Status: 200
[+] VULNERABLE: Payload: ' UNION SELECT NULL-- | Status: 200
```

---

⚙️ Available Tools

Category Tools
Vulnerability Scanners SQL Injection, XSS, LFI/RFI
Reconnaissance Admin Panel Finder, Directory Bruteforcer, Parameter Fuzzer
Network Tools Port Scanner, DNS Lookup, WHOIS Lookup
Utilities Hash Decrypter, Encoder/Decoder, HTTP Headers Check
Automation All-in-One Scan

---

📁 Project Structure

```
vulnterm/
├── hackbar/
│   ├── core/          # Core functionality (banner, colors, base)
│   ├── scanners/      # Vulnerability scanners
│   ├── tools/         # Utility tools
│   └── data/          # Payloads and wordlists
├── tests/             # Unit tests
├── docs/              # Documentation
├── run.py             # Entry point
├── setup.py           # Package setup
├── requirements.txt   # Dependencies
└── README.md          # This file
```

---

⚠️ Disclaimer

This tool is for educational and ethical hacking purposes only.

The author, Syed Rehan (@rehuux), does not condone any illegal or malicious use of this software. Users are solely responsible for ensuring they have explicit permission from the system owner before performing any security testing. Misuse of this tool may result in criminal prosecution.

Use responsibly and only on systems you own or have authorization to test.

---

🧪 Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test
python -m pytest tests/test_sqli.py -v
```

---

🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you want to contribute.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

---

📜 License

Distributed under the MIT License. See LICENSE for more information.

---

👤 Author

Syed Rehan (@rehuux)

· GitHub: @rehuux

---

🙏 Acknowledgements

· Inspired by various open-source security tools and frameworks.
· Built with Python and the open-source community.

```
