#!/usr/bin/env python3

import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hackbar.core.base import TerminalHackBar
from hackbar.scanners.sqli import scan_sqli, _test_sqli_payload
from hackbar.data.payloads import SQLI_PAYLOADS

class TestSQLIScanner(unittest.TestCase):
    """Test cases for SQL Injection Scanner"""
    
    def setUp(self):
        """Setup before each test"""
        self.app = TerminalHackBar()
        self.base_url = "https://example.com/page.php?id="
        self.test_payload = "' OR '1'='1"
    
    def test_sqli_payload_list_not_empty(self):
        """Test that SQLI_PAYLOADS is not empty"""
        self.assertGreater(len(SQLI_PAYLOADS), 0)
        self.assertIsInstance(SQLI_PAYLOADS, list)
    
    def test_sqli_payload_contains_common_payloads(self):
        """Test that common SQLi payloads are present"""
        common_payloads = [
            "'",
            "' OR '1'='1",
            "' UNION SELECT NULL--",
            "' AND SLEEP(5)--",
        ]
        for payload in common_payloads:
            self.assertIn(payload, SQLI_PAYLOADS)
    
    def test_sqli_payloads_are_strings(self):
        """Test that all SQLi payloads are strings"""
        for payload in SQLI_PAYLOADS:
            self.assertIsInstance(payload, str)
    
    def test_sqli_payloads_contain_quotes(self):
        """Test that SQLi payloads contain common SQL characters"""
        has_quote = any("'" in p for p in SQLI_PAYLOADS)
        self.assertTrue(has_quote)
        
        has_union = any("union" in p.lower() for p in SQLI_PAYLOADS)
        self.assertTrue(has_union)
    
    def test_scanner_function_exists(self):
        """Test that scan_sqli function exists"""
        self.assertTrue(callable(scan_sqli))
    
    def test_payload_test_function_exists(self):
        """Test that _test_sqli_payload function exists"""
        self.assertTrue(callable(_test_sqli_payload))
    
    def test_app_has_session(self):
        """Test that app has a session object"""
        self.assertIsNotNone(self.app.session)
        self.assertTrue(hasattr(self.app, 'session'))
    
    def test_app_has_timeout(self):
        """Test that app has timeout set"""
        self.assertEqual(self.app.timeout, 10)
        self.assertIsInstance(self.app.timeout, int)
    
    def test_app_has_max_threads(self):
        """Test that app has max_threads set"""
        self.assertEqual(self.app.max_threads, 10)
        self.assertIsInstance(self.app.max_threads, int)

if __name__ == "__main__":
    unittest.main()
