from phonemaster.database_service import PhoneMastHelper

large_divider = "---------------------------------"
small_divider = "--------"
introduction = "Phonemaster says:"

def _print_header(description):
    print(large_divider)
    print(introduction)
    print("-", description)

def view_rent_ascending(description, iterable_masts):
    def pretty_print_masts(someMast):
        tuple_rent_name_tenant = (PhoneMastHelper.rent(someMast), PhoneMastHelper.property_name(someMast), PhoneMastHelper.tenant_name(someMast))
        print("[%s] %s || %s" %tuple_rent_name_tenant)
    _print_header(description)
    print("- Format will be: [Rent] - Location Name || Tenant")
    print(small_divider)
    [pretty_print_masts(mast) for mast in iterable_masts]
    print(large_divider)

def view_lease_lengths_with_total(description, iterable_masts, total):
    _print_header(description)
    
    print(large_divider)

def view_mast_count_dict(description, tenant_name_count_dict):
    _print_header(description)

    print(large_divider)

def view_masts_in_date_range(description, iterable_masts):
    _print_header(description)

    print(large_divider)