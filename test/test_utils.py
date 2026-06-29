#!/usr/bin/env python3

import unittest
import sys
import os
import hashlib
import base64
import urllib.parse

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import all modules
from hackbar.core.base import TerminalHackBar
from hackbar.core.colors import Fore, Back, Style, init_colors
from hackbar.core.banner import print_banner
from hackbar.data.payloads import SQLI_PAYLOADS, XSS_PAYLOADS, LFI_PAYLOADS, ADMIN_PATHS
from hackbar.data.wordlists import HASH_DB, COMMON_PARAMS
from hackbar.tools.hash import _detect_hash_type, _crack_hash
from hackbar.scanners.lfi import scan_lfi

class TestUtils(unittest.TestCase):
    """Test cases for Utility functions"""
    
    def setUp(self):
        """Setup before each test"""
        self.app = TerminalHackBar()
    
    # ========== HASH TESTS ==========
    def test_hash_db_not_empty(self):
        """Test that HASH_DB is not empty"""
        self.assertGreater(len(HASH_DB), 0)
        self.assertIsInstance(HASH_DB, dict)
    
    def test_hash_db_contains_common_hashes(self):
        """Test that HASH_DB contains common password hashes"""
        self.assertIn("5f4dcc3b5aa765d61d8327deb882cf99", HASH_DB)
        self.assertEqual(HASH_DB["5f4dcc3b5aa765d61d8327deb882cf99"], "password")
        
        self.assertIn("21232f297a57a5a743894a0e4a801fc3", HASH_DB)
        self.assertEqual(HASH_DB["21232f297a57a5a743894a0e4a801fc3"], "admin")
    
    def test_hash_type_detection(self):
        """Test hash type detection"""
        # MD5 (32 chars)
        self.assertEqual(_detect_hash_type("5f4dcc3b5aa765d61d8327deb882cf99"), "MD5")
        
        # SHA1 (40 chars)
        self.assertEqual(_detect_hash_type("a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"), "SHA1")
        
        # SHA256 (64 chars)
        self.assertEqual(_detect_hash_type("5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"), "SHA256")
        
        # Unknown
        self.assertEqual(_detect_hash_type("abc123"), "Unknown")
    
    def test_crack_hash_md5(self):
        """Test MD5 hash cracking"""
        result = _crack_hash("5f4dcc3b5aa765d61d8327deb882cf99")
        self.assertEqual(result, "password")
        
        result = _crack_hash("21232f297a57a5a743894a0e4a801fc3")
        self.assertEqual(result, "admin")
    
    def test_crack_hash_unknown(self):
        """Test unknown hash cracking"""
        result = _crack_hash("unknownhash1234567890")
        self.assertIsNone(result)
    
    # ========== COMMON PARAMS TESTS ==========
    def test_common_params_not_empty(self):
        """Test that COMMON_PARAMS is not empty"""
        self.assertGreater(len(COMMON_PARAMS), 0)
        self.assertIsInstance(COMMON_PARAMS, list)
    
    def test_common_params_contains_common_parameters(self):
        """Test that COMMON_PARAMS contains common parameter names"""
        common = ["id", "page", "user", "password", "q", "search"]
        for param in common:
            self.assertIn(param, COMMON_PARAMS)
    
    # ========== BASE64 TESTS ==========
    def test_base64_encode_decode(self):
        """Test Base64 encoding and decoding"""
        text = "Hello World"
        encoded = base64.b64encode(text.encode()).decode()
        decoded = base64.b64decode(encoded).decode()
        self.assertEqual(decoded, text)
    
    # ========== URL TESTS ==========
    def test_url_encode_decode(self):
        """Test URL encoding and decoding"""
        text = "Hello World!"
        encoded = urllib.parse.quote(text)
        decoded = urllib.parse.unquote(encoded)
        self.assertEqual(decoded, text)
    
    # ========== HEX TESTS ==========
    def test_hex_encode_decode(self):
        """Test Hex encoding and decoding"""
        text = "Hello"
        encoded = text.encode().hex()
        decoded = bytes.fromhex(encoded).decode()
        self.assertEqual(decoded, text)
    
    # ========== COLORS TESTS ==========
    def test_colors_exist(self):
        """Test that color classes exist"""
        self.assertTrue(hasattr(Fore, 'RED'))
        self.assertTrue(hasattr(Fore, 'GREEN'))
        self.assertTrue(hasattr(Fore, 'YELLOW'))
        self.assertTrue(hasattr(Fore, 'CYAN'))
        self.assertTrue(hasattr(Back, 'RED'))
        self.assertTrue(hasattr(Style, 'RESET_ALL'))
    
    def test_init_colors_function_exists(self):
        """Test that init_colors function exists"""
        self.assertTrue(callable(init_colors))
    
    def test_colors_are_strings(self):
        """Test that all colors are strings"""
        color = Fore.RED
        self.assertIsInstance(color, str)
        
        style = Style.RESET_ALL
        self.assertIsInstance(style, str)
    
    # ========== BANNER TESTS ==========
    def test_print_banner_function_exists(self):
        """Test that print_banner function exists"""
        self.assertTrue(callable(print_banner))
    
    def test_print_banner_runs_without_error(self):
        """Test that print_banner runs without error"""
        try:
            print_banner()
            self.assertTrue(True)
        except Exception:
            self.fail("print_banner() raised an exception")
    
    # ========== PAYLOADS TESTS ==========
    def test_sqli_payloads_not_empty(self):
        """Test that SQLI_PAYLOADS is not empty"""
        self.assertGreater(len(SQLI_PAYLOADS), 0)
        self.assertIsInstance(SQLI_PAYLOADS, list)
    
    def test_xss_payloads_not_empty(self):
        """Test that XSS_PAYLOADS is not empty"""
        self.assertGreater(len(XSS_PAYLOADS), 0)
        self.assertIsInstance(XSS_PAYLOADS, list)
    
    def test_lfi_payloads_not_empty(self):
        """Test that LFI_PAYLOADS is not empty"""
        self.assertGreater(len(LFI_PAYLOADS), 0)
        self.assertIsInstance(LFI_PAYLOADS, list)
    
    def test_admin_paths_not_empty(self):
        """Test that ADMIN_PATHS is not empty"""
        self.assertGreater(len(ADMIN_PATHS), 0)
        self.assertIsInstance(ADMIN_PATHS, list)
    
    def test_all_payloads_are_strings(self):
        """Test that all payloads are strings"""
        for payload in SQLI_PAYLOADS:
            self.assertIsInstance(payload, str)
        
        for payload in XSS_PAYLOADS:
            self.assertIsInstance(payload, str)
        
        for payload in LFI_PAYLOADS:
            self.assertIsInstance(payload, str)
    
    # ========== APP TESTS ==========
    def test_app_has_hash_db(self):
        """Test that app has hash_db attribute"""
        self.assertTrue(hasattr(self.app, 'hash_db'))
        self.assertIsInstance(self.app.hash_db, dict)
    
    def test_app_has_print_methods(self):
        """Test that app has color print methods"""
        methods = [
            'print_red', 'print_green', 'print_yellow',
            'print_blue', 'print_cyan', 'print_magenta', 'print_white'
        ]
        for method in methods:
            self.assertTrue(hasattr(self.app, method))
            self.assertTrue(callable(getattr(self.app, method)))
    
    def test_app_has_session(self):
        """Test that app has a session object"""
        self.assertIsNotNone(self.app.session)
        self.assertTrue(hasattr(self.app, 'session'))
    
    def test_app_has_timeout(self):
        """Test that app has timeout set"""
        self.assertEqual(self.app.timeout, 10)
    
    def test_app_has_proxy(self):
        """Test that app has proxy attribute"""
        self.assertIsNone(self.app.proxy)
        self.assertTrue(hasattr(self.app, 'proxy'))
    
    def test_app_has_scanner_methods(self):
        """Test that app has scanner methods"""
        scanners = ['scan_sqli', 'scan_xss', 'scan_lfi', 'find_admin', 'scan_ports']
        for scanner in scanners:
            self.assertTrue(hasattr(self.app, scanner))
            self.assertTrue(callable(getattr(self.app, scanner)))
    
    def test_app_has_tool_methods(self):
        """Test that app has tool methods"""
        tools = ['hash_decrypt', 'encode_decode', 'brute_dirs', 'check_headers', 'fuzz_params', 'dns_lookup', 'whois_lookup']
        for tool in tools:
            self.assertTrue(hasattr(self.app, tool))
            self.assertTrue(callable(getattr(self.app, tool)))
    
    def test_app_has_about_method(self):
        """Test that app has about method"""
        self.assertTrue(hasattr(self.app, 'about'))
        self.assertTrue(callable(self.app.about))

if __name__ == "__main__":
    unittest.main()
