import csv
import os.path
from datetime import datetime

_csv_data = open(os.path.join(os.path.dirname(__file__), 'database.csv'))

def _date_formatter(date_string):
    return datetime.strptime(date_string, '%d %b %Y')

class PhoneMastHelper():
    @staticmethod
    def property_name(csv_row):
        return csv_row[0]

    @staticmethod
    def address(csv_row):
        return [csv_row[1], csv_row[2], csv_row[3], csv_row[4]]

    @staticmethod
    def unit_name(csv_row):
        return csv_row[5]

    @staticmethod
    def tenant_name(csv_row):
        return csv_row[6]

    @staticmethod
    def lease_start_date(csv_row):
        return _date_formatter(csv_row[7])

    @staticmethod
    def lease_end_date(csv_row):
        return _date_formatter(csv_row[8])
    
    @staticmethod
    def lease_years(csv_row):
        return int(csv_row[9])

    @staticmethod
    def rent(csv_row):
        print(csv_row)
        return float(csv_row[10])

    @staticmethod
    def validate_row(row):
        try:
            if (PhoneMastHelper.property_name(row) != "",
                PhoneMastHelper.address(row)[0] != "",
                PhoneMastHelper.unit_name(row) != "",
                PhoneMastHelper.tenant_name(row) != "",
                PhoneMastHelper.lease_start_date(row) is datetime,
                PhoneMastHelper.lease_end_date(row) is datetime,
                PhoneMastHelper.lease_years(row) != 0,
                PhoneMastHelper.rent(row) != 0):
                    return True
            else:
                return False
        except:
            return False


def get_masts_iterable():
    _csv_data.seek(0)
    reader = csv.reader(_csv_data)
    next(reader)
    return reader

"""
Check we have real data to work with
"""
if _csv_data is None:
    raise("Could not open CSV file")
for row in get_masts_iterable():
    if PhoneMastHelper.validate_row(row) == False:
        raise("One or more rows of the CSV file contains bad data")

print("Opened and validated CSV data, ready to go")