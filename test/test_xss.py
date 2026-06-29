#!/usr/bin/env python3

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hackbar.core.base import TerminalHackBar
from hackbar.scanners.xss import scan_xss, _test_xss_payload
from hackbar.data.payloads import XSS_PAYLOADS

class TestXSSScanner(unittest.TestCase):
    """Test cases for XSS Scanner"""
    
    def setUp(self):
        """Setup before each test"""
        self.app = TerminalHackBar()
        self.base_url = "https://example.com/search.php?q="
    
    def test_xss_payload_list_not_empty(self):
        """Test that XSS_PAYLOADS is not empty"""
        self.assertGreater(len(XSS_PAYLOADS), 0)
        self.assertIsInstance(XSS_PAYLOADS, list)
    
    def test_xss_payload_contains_common_payloads(self):
        """Test that common XSS payloads are present"""
        common_payloads = [
            "<script>alert(1)</script>",
            "<img src=x onerror=alert(1)>",
            "<svg onload=alert(1)>",
            "javascript:alert(1)",
        ]
        for payload in common_payloads:
            self.assertIn(payload, XSS_PAYLOADS)
    
    def test_xss_payloads_are_strings(self):
        """Test that all XSS payloads are strings"""
        for payload in XSS_PAYLOADS:
            self.assertIsInstance(payload, str)
    
    def test_xss_payloads_contain_script_tags(self):
        """Test that XSS payloads contain script tags or event handlers"""
        has_script = any("<script" in p.lower() for p in XSS_PAYLOADS)
        self.assertTrue(has_script)
        
        has_event = any("onerror" in p.lower() or "onload" in p.lower() for p in XSS_PAYLOADS)
        self.assertTrue(has_event)
    
    def test_scanner_function_exists(self):
        """Test that scan_xss function exists"""
        self.assertTrue(callable(scan_xss))
    
    def test_payload_test_function_exists(self):
        """Test that _test_xss_payload function exists"""
        self.assertTrue(callable(_test_xss_payload))
    
    def test_app_has_timeout(self):
        """Test that app has timeout set"""
        self.assertEqual(self.app.timeout, 10)
    
    def test_app_has_proxy(self):
        """Test that app has proxy attribute"""
        self.assertIsNone(self.app.proxy)
        self.assertTrue(hasattr(self.app, 'proxy'))

if __name__ == "__main__":
    unittest.main()
