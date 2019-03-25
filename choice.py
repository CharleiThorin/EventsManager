cake = {'Javas': 250000, 'BreadnCake': 200000, 'Sheraton': 90000, 'Biryani': 300000, 'CakeStudio': 150000,
        'HotLoaf': 170000, 'BBROAD': 200000, 'Haven': 140000}
photography = {'Malaika': 500000, 'ColorChrome': 460000, 'Fotogenix': 550000}
venues = {'ZionGardens': 2000000, 'NamirembeEvents': 2300000, 'FairwayHotel': 3000000}
florists = {'Rusadia': 500000, 'Flowers&Gifts': 460000, 'HelloServices': 6000000, 'Artecia': 700000}
bands = {'Faze2': 1000000, 'JazzVille': 1300000, 'zone7': 1100000}
caterers = {'Rendezvous': 3000000, 'DivineMercy': 2400000, 'serenaHotel': 6000000, 'BigMike': 5000000, }

total_budget = 0


def compare_prices(budget_value, category):
    current_budget_px = budget_value
    suppliers = []
    for key in category.keys():
        suppliers.append(key)
    current_supplier = suppliers[0]
    current_lowest_supplier_px = category[current_supplier]
    for vendor in suppliers:
        initial_vendor_px = current_lowest_supplier_px
        current_vendor_px = category[vendor]
        if current_vendor_px <= initial_vendor_px and current_vendor_px < current_lowest_supplier_px and \
                current_vendor_px < current_budget_px:
            current_lowest_supplier_px = current_vendor_px
            current_supplier = vendor
        if initial_vendor_px <= current_vendor_px < current_lowest_supplier_px and \
                current_vendor_px < current_budget_px:
            current_lowest_supplier_px = current_vendor_px
            current_supplier = vendor
    return {current_supplier: current_lowest_supplier_px}


def choose_cake(budget_value):
    return compare_prices(budget_value, cake)


def choose_photographer(budget_value):
    return compare_prices(budget_value, photography)


def choose_venue(budget_value):
    return compare_prices(budget_value, venues)


def choose_florist(budget_value):
    return compare_prices(budget_value, florists)


def choose_band(budget_value):
    return compare_prices(budget_value, bands)


def choose_caterer(budget_value):
    return compare_prices(budget_value, caterers)


cat_groups = {
    'cake': choose_cake(total_budget),
    'photography': choose_photographer(total_budget),
    'venue': choose_venue(total_budget),
    'florist': choose_florist(total_budget),
    'band': choose_band(total_budget),
    'caterer': choose_caterer(total_budget)
}

grps_one = []
grps_two = []

for item_key in cat_groups.keys():
    tuple_item = (item_key.lower(), item_key)
    if len(grps_one) != 3:
        grps_one.append(tuple_item)
    else:
        grps_two.append(tuple_item)


def choose_providers(groups, grps, budget):
    rem_budget = budget
    service_providers = {}
    for key in groups.keys():
        if key in grps:
            item = groups[key]
            if rem_budget > 0:
                for name, value in item.items():
                    item_supplier = name
                    supplier_price = value
                    if 0 < rem_budget < supplier_price and service_providers != {}:
                        msg = 'Your budget is too low to get other Items except those displayed with a price above'
                        return [msg, service_providers]
                    if 0 < rem_budget < supplier_price and service_providers == {}:
                        msg = 'Your budget is too low to get any of the Items listed in the table'
                        return [msg, service_providers]
                    service_providers[item_supplier] = supplier_price
                    rem_budget = rem_budget - supplier_price
            else:
                msg = 'Your budget is too low to get the Items selected'
                return [msg, service_providers]
    msg = 'Your remaining budget is UGX: ' + str(rem_budget)
    return [msg, service_providers]


def item_distro(groups, grp_key):
    distros = {}
    for key in grp_key:
        item = groups[key]
        for distro in item.keys():
            distros[key] = distro
    print(distros)
    return distros


# print(choose_providers(cat_groups, ['photography', 'venue', 'florist', 'caterer'], total_budget))
# item_distro(cat_groups, ['photography', 'venue', 'florist', 'caterer'])
