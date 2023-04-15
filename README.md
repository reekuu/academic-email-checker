# Academic Email Checker

This repository contains a Python script that checks whether an email address is associated with an academic institution.

The script prompts users to enter an email address, and it verifies the domain against a list of known academic and public domains.

## Data Sources

- academic_domains: https://github.com/Hipo/university-domains-list
- public_domains: https://gist.github.com/tbrianjones/5992856

## Requirements

- Python 3.x
- CSV files containing academic and public email domains

## Run the script

    python email_checker.py -e <valid email address>

Ensure that the `academic_domains.csv` and `public_domains.csv` files are downloaded and located in the `data` folder.

Update these files with the appropriate domain data if needed.

The script will prompt you to enter an email address. Follow the instructions provided by the script.

## Test cases
    test_cases = [
        'someone@univie.ac.at',
        'someone@gmail.com',
        'someone@ucsd.edu',
        'someone@ens.psl.eu',
        'someone@ax.sub.education',
        'someone@isu.edu',
        'someone@psy.fsu.edu',
        'someone@st.swps.edu.pl',
        'someone@hortonworks.ace',
        'someone@uni-bonn.de',
        'someone@twu.edu',
        'someone@academy.acer.com',
        'someone@mail.huji.ac.il',
        'someone@soton.ac.uk',
        'someone@edutain.me',
    ]
