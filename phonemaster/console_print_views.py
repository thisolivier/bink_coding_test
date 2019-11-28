from phonemaster.database_service import PhoneMastHelper
from datetime import datetime

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
    print("- Format will be: [Rent] - Mast Location || Tenant")
    print(small_divider)
    [pretty_print_masts(mast) for mast in iterable_masts]
    print(large_divider)

def view_lease_lengths_with_total(description, iterable_masts, total_rent):
    _print_header(description)
    print("- Matching masts will be printed with the following ordered fields:")
    print("Property Name, Property Address [1], Property  Address [2], Property Address [3], Property Address [4], Unit Name, Tenant Name, Lease Start Date, Lease End Date, Lease Years, Current Rent")
    print(small_divider)
    [print(mast) for mast in iterable_masts]
    print(small_divider)
    print("Total rent for above masts:", total_rent)
    print(large_divider)

def view_mast_count_dict(description, tenant_name_count_dict):
    def pretty_print_tenants(name, count):
        print("[%s] - %s" %(count, name))

    _print_header(description)
    print("- Format will be: [Number of Masts] - Tenant")
    print(small_divider)
    [pretty_print_tenants(tenant_name, count) for tenant_name, count in tenant_name_count_dict.items()]
    print(large_divider)

def view_masts_in_date_range(description, iterable_masts):
    def pretty_print_masts(mast):
        date = PhoneMastHelper.lease_start_date(mast)
        formatted_date = date.strftime("%d %m %Y")
        date_mast_tenant_tuple = (formatted_date, PhoneMastHelper.property_name(mast), PhoneMastHelper.tenant_name(mast))
        print("[%s] %s || %s" %date_mast_tenant_tuple)

    _print_header(description)
    print("- Format will be: [date] - Mast location || Tenant")
    print(small_divider)
    [pretty_print_masts(mast) for mast in iterable_masts]
    print(large_divider)