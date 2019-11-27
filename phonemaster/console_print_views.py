from database_service import PhoneMastHelper

large_divider = "---------------------------------"
small_divider = "--------"
introduction = "Phonemaster says:"

def rent_view(description, iterableMasts):
    def pretty_print_masts(someMast):
        tuple_rent_name_tenant = (PhoneMastHelper.rent(someMast), PhoneMastHelper.property_name(someMast), PhoneMastHelper.tenant_name(someMast))
        print("[%s] %s || %s" %tuple_rent_name_tenant)

    print(large_divider)
    print(introduction)
    print("-", description)
    print("- Format will be: [Rent] - Location Name || Tenant")
    print(small_divider)
    [pretty_print_masts(mast) for mast in iterableMasts]
    print(large_divider)