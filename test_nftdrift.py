# test_nftdrift.py
"""
Tests for NFTDrift module.
"""

import unittest
from nftdrift import NFTDrift

class TestNFTDrift(unittest.TestCase):
    """Test cases for NFTDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NFTDrift()
        self.assertIsInstance(instance, NFTDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NFTDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
