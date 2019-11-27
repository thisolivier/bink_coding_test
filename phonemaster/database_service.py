import csv
import os.path

_csv_data = open(os.path.join(os.path.dirname(__file__), 'database.csv'))

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
        return csv_row[7]

    @staticmethod
    def lease_end_date(csv_row):
        return csv_row[8]
    
    @staticmethod
    def lease_years(csv_row):
        print("years", csv_row[9])
        return int(csv_row[9])

    @staticmethod
    def rent(csv_row):
        return csv_row[10]

def get_masts_iterable():
    _csv_data.seek(1)
    reader = csv.reader(_csv_data)
    _csv_data.seek(1)
    return reader


