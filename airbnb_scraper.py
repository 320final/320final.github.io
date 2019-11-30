from bs4 import BeautifulSoup as bs
import requests
import urllib
import json
import time
import collections
import pprint
import csv

url = "https://www.airbnb.com/api/v2/explore_tabs?_format=for_explore_search_web&auto_ib=false&client_session_id=12c460bd-4911-4462-855f-dca1778fd776&currency=USD&current_tab_id=home_tab&experiences_per_grid=20&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&hide_dates_and_guests_filters=false&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_per_grid=18&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=en&metadata_only=false&query=New%20York%2C%20NY%2C%20United%20States&query_understanding_enabled=true&refinement_paths%5B%5D=%2Fhomes&satori_version=1.1.14&screen_height=969&screen_size=medium&screen_width=1114&selected_tab_id=home_tab&show_groupings=true&supports_for_you_v3=true&timezone_offset=-360&version=1.6.5"

data_dict = []

for i in range(0,20):
    print(i)
    with open('{}page.json'.format(i), 'r', encoding="utf8") as file:
        data = json.load(file)

    print(data)
    if i == 0:
        print("yo")
        homes = data.get('explore_tabs')[0].get('sections')[1].get('listings')
    else:
        homes = data.get('explore_tabs')[0].get('sections')[0].get('listings')
        print("fo")
    for home in homes:
        obj = {
            "room_id": "{}".format(str(home.get('listing').get('id'))),
            "name": "{}".format(str(home.get('listing').get('name'))),
            "neighborhood": "{}".format(home.get('listing').get('neighborhood')),
            "person_cap": "{}".format(home.get('listing').get('person_capacity')),
            "bedrooms": "{}".format(home.get('listing').get('beds')),
            "bathrooms": "{}".format(home.get('listing').get('bathrooms')),
            "amenities": "{}".format(home.get('listing').get('preview_amenities')),
            "reviews": "{}".format(home.get('listing').get('reviews_count')),
            "prop_type": "{}".format(home.get('listing').get('room_and_property_type')),
            "guests": "{}".format(home.get('listing').get('guest_label')),
            "star": "{}".format(home.get('listing').get('star_rating')),
            "avg_rating": "{}".format(home.get('listing').get('avg_rating')),
            "min_nights": "{}".format(home.get('listing').get('min_nights')),
            "max_nights": "{}".format(home.get('listing').get('max_nights')),
            "price": "{}".format(home.get('pricing_quote').get('rate').get('amount'))
        }
        data_dict.append(obj)
f = open("sample.csv", "w", encoding='utf-8')
writer = csv.DictWriter(
    f, fieldnames=["room_id", "name", "neighborhood", "person_cap", "bedrooms", "bathrooms",
    "amenities", "reviews", "prop_type", "guests", "star", "avg_rating", "min_nights",
    "max_nights", "price"])
writer.writeheader()
writer.writerows(data_dict)
printer = pprint.PrettyPrinter()
printer.pprint(data_dict)
