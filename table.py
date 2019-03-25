import copy

'''
JSON STRUCTURE
[
    {
        cake:{
            dist:"",
            price:""
        },
        photography:{
            dist:"",
            price:""
        },
        venues:{
            dist:"",
            price:""
        },
        florists:{
            dist:"",
            price:""
        },
        bands:{
            dist:"",
            price:""
        },
        caterers:{
            dist:"",
            price:""
        }
    }
]

'''

providers = {
    "cake": {'Javas': 250000, 'BreadnCake': 200000, 'Sheraton': 90000, 'Biryani': 300000, 'CakeStudio': 150000,
             'HotLoaf': 170000, 'BBROAD': 200000, 'Haven': 140000},
    "photography": {'Malaika': 500000, 'ColorChrome': 460000, 'Fotogenix': 550000},
    "venues": {'ZionGardens': 2000000, 'NamirembeEvents': 2300000, 'FairwayHotel': 3000000},
    "florists": {'Rusadia': 500000, 'Flowers&Gifts': 460000, 'HelloServices': 6000000, 'Artecia': 700000},
    "bands": {'Faze2': 1000000, 'JazzVille': 1300000, 'zone7': 1100000},
    "caterers": {'Rendezvous': 3000000, 'DivineMercy': 2400000, 'serenaHotel': 6000000, 'BigMike': 5000000, }
}


def populate_table():
    provider_type_lengths = []
    row_skeleton = {}

    for provider_type in providers:
        item_length = len(providers[provider_type])
        provider_type_lengths.append(item_length)
        row_skeleton[provider_type] = {"dist": "", "price": ""}

    row_no = max(provider_type_lengths)

    rows = [copy.copy(row_skeleton) for i in range(row_no)]

    for provider_type in providers:
        provider_type_idx = 0
        provider_type_obj = providers[provider_type]
        for dist in provider_type_obj:
            provider_obj = {"dist": dist, "price": provider_type_obj[dist]}
            rows[provider_type_idx][provider_type] = provider_obj
            provider_type_idx = provider_type_idx + 1
    return rows


#populate_table()
# import json
# print(json.dumps(rows))