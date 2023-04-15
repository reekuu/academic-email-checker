import re


def extract_domain(email):
    """Extract the domain part from an email address"""
    return email.split('@')[-1].strip().lower()


def is_valid_email(email):
    """Check if the email is valid."""
    if not email:
        return False
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(email_pattern, email))
