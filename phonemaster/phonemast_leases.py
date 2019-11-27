from database_service import get_masts_iterable, PhoneMastHelper
from console_print_views import rent_view

_get_masts_iterable = get_masts_iterable

def current_rent_ascending_order():
    """ Requirements
    1) Produce a list sorted by “Current Rent” in ascending order
    2) Obtain the first 5 items from the resultant list and output to the console
    """
    masts_sorted_by_rent = sorted(_get_masts_iterable(), key=PhoneMastHelper.rent)[:5]
    description = "The first five items in list of masts sorted by rent"
    rent_view(description, masts_sorted_by_rent)
    return masts_sorted_by_rent

def lease_length_25_years():
    """ Requirements
    1) Output the list to the console, including all data fields
    2) Output the total rent for all items in this list to the console
    """
    masts_with_25_year_lease = [mast for mast in _get_masts_iterable() if PhoneMastHelper.lease_years(mast) == 25]
    total_rents = 0.0
    for mast in masts_with_25_year_lease:
        total_rents += PhoneMastHelper.rent(mast)
    print(total_rents)
    return (masts_with_25_year_lease, total_rents)

def masts_count_per_tenant():
    """ Requirements
    1) Output the dictionary to the console in a readable form
    """
    pass

def lease_start_date_1june1999_to_31aug2007():
    """ Requirements
    1) Output the data to the console with dates formatted as DD/MM/YYYY
    """
    pass

if __name__ == '__main__':
    lease_length_25_years()