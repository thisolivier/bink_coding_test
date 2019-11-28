from datetime import datetime
from phonemaster.database_service import get_masts_iterable, PhoneMastHelper
from phonemaster.console_print_views import view_rent_ascending, view_masts_in_date_range, view_mast_count_dict, view_lease_lengths_with_total

class PhonemastLeaseTools:
    def __init__(self, get_mast_iterable = get_masts_iterable, print_results = True):
        self._get_masts_iterable = get_mast_iterable
        self._print_results = print_results

    def current_rent_ascending_order(self):
        """ Requirements
        1) Produce a list sorted by “Current Rent” in ascending order
        2) Obtain the first 5 items from the resultant list and output to the console
        """
        masts_sorted_by_rent = sorted(self._get_masts_iterable(), key=PhoneMastHelper.rent)[:5]

        if self._print_results:
            description = "The first five items in list of masts sorted by rent"
            view_rent_ascending(description, masts_sorted_by_rent)
            return

        return masts_sorted_by_rent

    def lease_length_25_years(self):
        """ Requirements
        1) Output the list to the console, including all data fields
        2) Output the total rent for all items in this list to the console
        """
        masts_with_25_year_lease = [mast for mast in self._get_masts_iterable() if PhoneMastHelper.lease_years(mast) == 25]
        total_rent = 0.0
        for mast in masts_with_25_year_lease:
            total_rent += PhoneMastHelper.rent(mast)

        if self._print_results:
            description = "All phone masts with 25 year leases, and their total rent"
            view_lease_lengths_with_total(description, masts_with_25_year_lease, total_rent)
            return

        return (masts_with_25_year_lease, total_rent)

    def masts_count_per_tenant(self):
        """ Requirements
        1) Output the dictionary to the console in a readable form
        """
        tenants_dict = {}
        for mast in self._get_masts_iterable():
            tenant = PhoneMastHelper.tenant_name(mast)
            if tenant in tenants_dict:
                tenants_dict[tenant] += 1
            else:
                tenants_dict[tenant] = 1
        
        if self._print_results:
            description = "Tenants names and the number of masts they lease"
            view_mast_count_dict(description, tenants_dict)
            return

        return tenants_dict

    def lease_start_date_1june1999_to_31aug2007(self):
        """ Requirements
        1) Output the data to the console with dates formatted as DD/MM/YYYY
        """
        range_start = datetime(1999, 6, 1)
        range_end = datetime(2007, 7, 31)
        def filter_only_in_range(mast):
            lease_start = PhoneMastHelper.lease_start_date(mast)
            return range_start < lease_start < range_end

        masts_in_range = list(filter(filter_only_in_range, self._get_masts_iterable()))
        
        if self._print_results:
            description = "Masts with a lease starting between 01/06/1999 and 31/07/2007"
            view_masts_in_date_range(description, masts_in_range)
            return

        return masts_in_range

    def run_all_queries(self):
        self.current_rent_ascending_order()
        self.lease_length_25_years()
        self.masts_count_per_tenant()
        self.lease_start_date_1june1999_to_31aug2007()
        print("Thanks for executing, have a nice day!")

phonemast_lease_tools = PhonemastLeaseTools()