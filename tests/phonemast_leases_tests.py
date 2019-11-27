import os
import unittest

from context import PhonemastLeaseTools

def _get_dummy_data(): return [
    ["Location Hawai","Address Hawai","","","PostCode Hawai","Unit Hawai","Tenant Hawai","31 Aug 2007","28 Feb 2058","25","10.00"],
    ["Location Kent","Address Kent","","","PostCode Kent","Unit Kent","Tenant Kent","01 Jun 1999","28 Feb 2058","4","9.00"],
    ["Location Mordor","Address Mordor","","","PostCode Mordor","Unit Mordor","Sauron","06 Dec 2000","28 Feb 2058","-4","8.00"],
    ["Location Valhalla","Address Valhalla","","","PostCode Valhalla","Unit Valhalla","Odin","20 Mar 50","28 Feb 20058","25","7.50"],
    ["Location Seattle","Address Seattle","","","PostCode Seattle","Unit Seattle","Tenant Seattle","12 Aug 2004","28 Feb 20058","24","6.01"],
    ["Location Ascot","Address Ascot","","","PostCode Ascot","Unit Ascot","Tenant Ascot","29 Feb 2002","28 Feb 20058","26","4.00"]
]

_phonemast_lease_tools = PhonemastLeaseTools(_get_dummy_data, False)

class CurrentRentTest(unittest.TestCase):
    def test_get_five_results(self):
        result = _phonemast_lease_tools.current_rent_ascending_order()
        assert len(result) == 5

    def test_results_are_ascending(self):
        result = _phonemast_lease_tools.current_rent_ascending_order()
        first_result_rent = result[0][10]
        middle_result_rent = result[2][10]
        last_result_rent = result[4][10]
        print(first_result_rent, middle_result_rent, last_result_rent)
        assert first_result_rent <= middle_result_rent <= last_result_rent

    def test_results_start_at_beginning(self):
        result = _phonemast_lease_tools.current_rent_ascending_order()
        assert result[0][0] == "Location Ascot"

class LeaseLength25YearsTest(unittest.TestCase):
    def test_correct_count(self):
        pass

    def test_returns_all_fields(self):
        pass

    def test_correct_total(self):
        pass

class MastsCountPerTenantTest(unittest.TestCase):
    def test_correct_number_of_tenants(self):
        pass

    def test_correct_masts_per_tenant(self):
        pass

class LeaseDateRangeTest(unittest.TestCase):
    def test_start_date_within_range(self):
        pass

    def test_count_is_correct(self):
        pass

    def test_date_format(self):
        pass

if __name__ == "__main__":
    unittest.main()