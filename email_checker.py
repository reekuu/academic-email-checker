import argparse
import csv
import subprocess
import re

from common import extract_domain, is_valid_email
from constants import ACADEMIC_DOMAINS_FILE, PUBLIC_DOMAINS_FILE


def load_domains_from_csv(filename):
    """Load the list of domains from the CSV file."""
    with open(filename, 'r') as csvfile:
        return [row['domain'] for row in csv.DictReader(csvfile, delimiter=',')]


def has_academic_substring(domain):
    """Check if the domain has an academic substring (e.g., ".ac." or ".edu")."""
    academic_pattern = r'\.ac\.|\.edu(?:$|\.)'
    return bool(re.search(academic_pattern, domain))


def main(email=None):
    """Main function for the academic email checker script.

    Prompts the user for an email address and checks if it is an academic email.
    """
    # Load academic and public domains from the CSV files
    academic_domains = load_domains_from_csv(ACADEMIC_DOMAINS_FILE)
    public_domains = load_domains_from_csv(PUBLIC_DOMAINS_FILE)

    # Prompt the user for a valid email address
    while not is_valid_email(email):
        email = input('\nEnter your academic email address: ')

    # Extract the domain from the entered email address
    domain = extract_domain(email)

    # Check if the domain is public, academic, or unrecognized
    if domain in public_domains:
        print('\n[DECLINE]', 'Please provide an academically affiliated email address.')
    elif domain in academic_domains or has_academic_substring(domain):
        print('\n[ACCEPT]', 'Verification link sent to your email. Please check your inbox.')
        print('''\nLet's imagine that the user clicked on a link from an email. Then they will see:''')
        subprocess.run(['python', 'user_affiliation.py', '-e', email])
    else:
        print('\n[MODERATION]', 'University is not recognized. It will be manually verified.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Academic email checker script.')
    parser.add_argument('-e', '--email', type=str, help='Email address to check.')
    args = parser.parse_args()
    main(email=args.email)
