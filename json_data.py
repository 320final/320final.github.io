import json
import time
import collections
import pprint

with open('firstpage.json', 'r') as file:
    data = json.load(file)

homes = data.get('explore_tabs')[0].get('sections')[1].get('listings')

data_dict = collections.defaultdict(dict)

for home in homes:
    room_id = str(home.get('listing').get('id'))
    data_dict[room_id]['name'] = str(home.get('listing').get('name'))
    data_dict[room_id]['neighborhood'] = home.get('listing').get('neighborhood')
    data_dict[room_id]['person_cap'] = home.get('listing').get('person_capacity')
    data_dict[room_id]['bedrooms'] = home.get('listing').get('beds')
    data_dict[room_id]['bathrooms'] = home.get('listing').get('bathrooms')
    data_dict[room_id]['amenities'] = home.get('listing').get('preview_amenities')
    data_dict[room_id]['reviews'] = home.get('listing').get('reviews_count')
    data_dict[room_id]['prop_type'] = home.get('listing').get('room_and_property_type')
    data_dict[room_id]['guests'] = home.get('listing').get('guest_label')
    data_dict[room_id]['star'] = home.get('listing').get('star_rating')
    data_dict[room_id]['avg_rating'] = home.get('listing').get('avg_rating')
    data_dict[room_id]['min_nights'] = home.get('listing').get('min_nights')
    data_dict[room_id]['max_nights'] = home.get('listing').get('max_nights')
    data_dict[room_id]['price'] = home.get('pricing_quote').get('rate').get('amount')

printer = pprint.PrettyPrinter()
printer.pprint(data_dict)

