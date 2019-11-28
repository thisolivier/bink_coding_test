# Olivier's Technical Test for Bink

## Requirements
* Python 3.5 or newer

## Installing
*Unless specified, all futher commands should be typed into your terminal*
1. Ensure you're running Python 3.5 or higher by entering `python --version`
2. This project only relies on Python standard libraries, there's nothing else to install

## Query stores from the terminal
*Unless specified, all futher commands should be typed into your terminal*
1. Open terminal and navigate to the root of this project.
2. Enter the python shell by entering `python` into your terminal
3. Enter `from phonemaster.phonemast_lease_tools import phonemast_lease_tools`
4. For individual queries:
    * To sort phone masts by rent and see the first 5, enter `phonemast_lease_tools.current_rent_ascending_order()`
    * To see all masts with a lease of 25 years, enter `phonemast_lease_tools.lease_length_25_years()`
    * To see the number of masts each tenant leases, enter `phonemast_lease_tools.masts_count_per_tenant()`
    * To see only those masts with lease start dates between 1st June 1999 and 31st August 2007, enter `phonemast_lease_tools.lease_start_date_1june1999_to_31aug2007()`
5. To run all queries, enter `phonemast_lease_tools.run_all_queries()`

## Testing

1. Open terminal and navigate to the root of this project
2. Enter `python tests/phonemast_leases_tests.py`

## *Thanks very much for the challenge, I'd love a code review, Olivier*