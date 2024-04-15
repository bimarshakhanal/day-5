import unittest
import re

EMAIL_REGEX = r'^[\w\.\_]+@[a-zA-Z]+.[A-Za-z\.]+'


def validate_email(email: str) -> bool:
    """
    Validates an email address based on format and common providers (excluding disposables).

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Check for space and @
    if not re.match(EMAIL_REGEX, email):
        return False

    # Check for valid service provider
    _, domain = email.split('@')

    # Check for common providers
    valid_providers = {"gmail.com", "yahoo.com", "outlook.com"}
    return domain.lower() in valid_providers


class TestEmail(unittest.TestCase):
    '''Unittest to test validate_email function'''

    def test_valid_email(self):
        '''Test for valid email address'''
        self.assertTrue(validate_email('user123_456@yahoo.com'))
        self.assertTrue(validate_email('user@yopmail.com'))
        self.assertTrue(validate_email('username with spaces@domain.com'))
        self.assertTrue(validate_email('asdff'))
        self.assertTrue(validate_email('asdff@gmail.com'))


if __name__ == '__main__':
    unittest.main()
