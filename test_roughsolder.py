# test_roughsolder.py
"""
Tests for RoughSolder module.
"""

import unittest
from roughsolder import RoughSolder

class TestRoughSolder(unittest.TestCase):
    """Test cases for RoughSolder class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RoughSolder()
        self.assertIsInstance(instance, RoughSolder)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RoughSolder()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
