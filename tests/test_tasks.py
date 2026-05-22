import unittest
from utils.validator import Validator

class TestValidator(unittest.TestCase):

    def test_valid_priority(self):
        self.assertTrue(Validator.validate_priority("high"))
        self.assertTrue(Validator.validate_priority("low"))
        self.assertTrue(Validator.validate_priority("medium"))

    def test_invalid_priority(self):
        with self.assertRaises(ValueError):
            Validator.validate_priority("urgent")


    def test_valid_deadline(self):
        self.assertTrue(Validator.validate_deadline("2026-06-01"))

    def test_invalid_deadline(self):
        with self.assertRaises(ValueError):
            Validator.validate_deadline("01-06-2026")
        with self.assertRaises(ValueError):
            Validator.validate_deadline("2026/06/01")

    def test_valid_status(self):
        self.assertTrue(Validator.validate_status("pending"))
        self.assertTrue(Validator.validate_status("completed"))

    def test_invalid_status(self):
        with self.assertRaises(ValueError):
            Validator.validate_status("done")

if __name__ == "__main__":
    unittest.main()
