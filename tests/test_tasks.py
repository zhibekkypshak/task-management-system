import unittest
from utils.validator import Validator

class TestValidator(unittest.TestCase):

    def test_valid_priority(self):
        self.assertTrue(Validator.validate_priority("high"))
        self.assertTrue(Validator.validate_priority("low"))
        self.assertTrue(Validator.validate_priority("medium"))

