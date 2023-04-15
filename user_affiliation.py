import argparse
import csv

from common import extract_domain, is_valid_email
from constants import ACADEMIC_DOMAINS_FILE, DOMAINS_FOR_MODERATION_FILE, USERS_FILE


def append_row_to_csv(filename, input_row):
    """Appends a row to the given CSV file."""
    with open(filename, mode='a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(input_row)


def main(email=None, user_input=''):
    """Main function to run the script."""
    # Prompt the user for a valid email address and extract the domain
    while not is_valid_email(email):
        email = input('\nEnter the correct email from the previous step: ')
    domain = extract_domain(email)

    # Search for the domain in the academic domains file
    with open(ACADEMIC_DOMAINS_FILE, mode='r') as csvfile:
        for row in csv.DictReader(csvfile, delimiter=','):
            if row['domain'] == domain:
                # If the domain is found, confirm the affiliation and country
                affiliation = row['name']
                user_input = input(f'\nIs {affiliation}, {row["country"]} your primary affiliation? (yes/no) ')
                break

    if user_input.lower() not in {'y', 'yes'}:
        affiliation = input('\nWhat is the name of your primary affiliation?: ')
        country = input('\nWhat is the country of your primary affiliation?: ')
        # Add the domain and affiliation to the domains for moderation file
        append_row_to_csv(DOMAINS_FOR_MODERATION_FILE, [domain, affiliation, country])
        print('\n[INFO]', f'({domain}, {affiliation}, {country}) recorded for the manual moderation.')

    # Add the email address and affiliation to the users file
    append_row_to_csv(USERS_FILE, [email, affiliation])
    print('\n[INFO]', f'({email}, {affiliation}) new user record successfully added.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Affiliation checker script.')
    parser.add_argument('-e', '--email', type=str, help='Email address to check.')
    args = parser.parse_args()
    main(email=args.email)
