from bs4 import BeautifulSoup as bs
import requests
import urllib
import json
import time
import collections
import pprint
import csv

states = {
    'Alabama': 'ChIJdf5LHzR_hogR6czIUzU0VV4',
    'Alaska': 'ChIJG8CuwJzfAFQRNduKqSde27w',
    'Arizona': 'ChIJaxhMy-sIK4cRcc3Bf7EnOUI',
    'Arkansas': 'ChIJYSc_dD-e0ocR0NLf_z5pBaQ',
    'California': 'ChIJPV4oX_65j4ARVW8IJ6IJUYs',
    'Colorado': 'ChIJt1YYm3QUQIcR_6eQSTGDVMc',
    'Connecticut': 'ChIJpVER8hFT5okR5XBhBVttmq4',
    'Delaware': 'ChIJO9YMTXYFx4kReOgEjBItHZQ',
    'Florida': 'ChIJvypWkWV2wYgR0E7HW9MTLvc',
    'Georgia': 'ChIJV4FfHcU28YgR5xBP7BC8hGY',
    'Idaho': 'ChIJ6Znkhaj_WFMRWIf3FQUwa9A',
    'Illinois': 'ChIJGSZubzgtC4gRVlkRZFCCFX8',
    'Indiana': 'ChIJHRv42bxQa4gRcuwyy84vEH4',
    'Iowa': 'ChIJGWD48W9e7ocR2VnHV0pj78Y',
    'Kansas': 'ChIJawF8cXEXo4cRXwk-S6m0wmg',
    'Kentucky': 'ChIJyVMZi0xzQogR_N_MxU5vH3c',
    'Louisiana': 'ChIJZYIRslSkIIYRA0flgTL3Vck',
    'Maine': 'ChIJ1YpTHd4dsEwR0KggZ2_MedY',
    'Maryland': 'ChIJ35Dx6etNtokRsfZVdmU3r_I',
    'Massachusetts': 'ChIJ_b9z6W1l44kRHA2DVTbQxkU',
    'Michigan': 'ChIJEQTKxz2qTE0Rs8liellI3Zc',
    'Minnesota': 'ChIJmwt4YJpbWE0RD6L-EJvJogI',
    'Mississippi': 'ChIJGdRK5OQyKIYR2qbc6X8XDWI',
    'Missouri': 'ChIJfeMiSNXmwIcRcr1mBFnEW7U',
    'Montana': 'ChIJ04p7LZwrQVMRGGwqz1jWcfU',
    'Nebraska': 'ChIJ7fwMtciNk4cRxArzDwyQJ6E',
    'Nevada': 'ChIJcbTe-KEKmYARs5X8qooDR88',
    'New Hampshire': 'ChIJ66bAnUtEs0wR64CmJa8CyNc',
    'New Jersey': 'ChIJn0AAnpX7wIkRjW0_-Ad70iw',
    'New Mexico': 'ChIJqVKY50NQGIcRup41Yxpuv0Y',
    'New York': 'ChIJqaUj8fBLzEwRZ5UY3sHGz90',
    'North Carolina': 'ChIJgRo4_MQfVIgRGa4i6fUwP60',
    'North Dakota': 'ChIJY-nYVxKD11IRyc9egzmahA0',
    'Ohio': 'ChIJwY5NtXrpNogRFtmfnDlkzeU',
    'Oklahoma': 'ChIJnU-ssRE5rIcRSOoKQDPPHF0',
    'Oregon': 'ChIJVWqfm3xuk1QRdrgLettlTH0',
    'Pennsylvania': 'ChIJieUyHiaALYgRPbQiUEchRsI',
    'Rhode Island': 'ChIJD9cOYhQ15IkR5wbB57wYTh4',
    'South Carolina': 'ChIJ49ExeWml-IgRnhcF9TKh_7k',
    'South Dakota': 'ChIJpTjphS1DfYcRt6SGMSnW8Ac',
    'Tennessee': 'ChIJA8-XniNLYYgRVpGBpcEgPgM',
    'Texas': 'ChIJSTKCCzZwQIYRPN4IGI8c6xY',
    'Utah': 'ChIJzfkTj8drTIcRP0bXbKVK370',
    'Vermont': 'ChIJ_87aSGzctEwRtGtUNnSJTSY',
    'Virginia': 'ChIJzbK8vXDWTIgRlaZGt0lBTsA',
    'Washington': 'ChIJ-bDD5__lhVQRuvNfbGh4QpQ'
}

data_dict = []

for state in states:
    id = states[state]
    state = state.replace(" ", "%20")
    print(state)
    url = "https://www.airbnb.com/api/v2/explore_tabs?_format=for_explore_search_web&auto_ib=false&client_session_id=7a1719fb-5452-4be6-8040-45e57eddd9c8&currency=USD&current_tab_id=home_tab&experiences_per_grid=20&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&hide_dates_and_guests_filters=false&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_per_grid=18&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=en&metadata_only=false&query={}%2C%20United%20States&query_understanding_enabled=true&refinement_paths%5B%5D=%2Fhomes&satori_version=1.1.14&screen_height=969&screen_size=medium&screen_width=1114&selected_tab_id=home_tab&show_groupings=true&supports_for_you_v3=true&timezone_offset=-360&version=1.6.5".format(state)

    for i in range(0,20):
        if i == 0:
            response = requests.get(url)
            print(response)
            page = urllib.request.urlopen(url)
            print(page)
            soup = bs(page, "html.parser")
            print(soup)

            output = "0{}page.json".format(state)
            with open(output, 'wb') as f:
                f.write(str(soup).encode())
            
        else:
            response = requests.get("https://www.airbnb.com/api/v2/explore_tabs?_format=for_explore_search_web&auto_ib=false&client_session_id=7a1719fb-5452-4be6-8040-45e57eddd9c8&currency=USD&current_tab_id=home_tab&experiences_per_grid=20&federated_search_session_id=0360991d-1087-4e46-a106-d5090e86351d&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&hide_dates_and_guests_filters=false&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_offset={}&items_per_grid=18&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&last_search_session_id=b58af588-7a00-48a0-b9ff-10d3c4a47a52&locale=en&metadata_only=false&place_id={}&query={}%2C%20United%20States&query_understanding_enabled=true&refinement_paths%5B%5D=%2Fhomes&s_tag=X74Q583S&satori_version=1.1.14&screen_height=969&screen_size=medium&screen_width=1114&search_type=pagination&section_offset=4&selected_tab_id=home_tab&show_groupings=true&supports_for_you_v3=true&timezone_offset=-360&version=1.6.5".format(i*18,id,state))
            print(response)
            page = urllib.request.urlopen("https://www.airbnb.com/api/v2/explore_tabs?_format=for_explore_search_web&auto_ib=false&client_session_id=7a1719fb-5452-4be6-8040-45e57eddd9c8&currency=USD&current_tab_id=home_tab&experiences_per_grid=20&federated_search_session_id=0360991d-1087-4e46-a106-d5090e86351d&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&hide_dates_and_guests_filters=false&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_offset={}&items_per_grid=18&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&last_search_session_id=b58af588-7a00-48a0-b9ff-10d3c4a47a52&locale=en&metadata_only=false&place_id={}&query={}%2C%20United%20States&query_understanding_enabled=true&refinement_paths%5B%5D=%2Fhomes&s_tag=X74Q583S&satori_version=1.1.14&screen_height=969&screen_size=medium&screen_width=1114&search_type=pagination&section_offset=4&selected_tab_id=home_tab&show_groupings=true&supports_for_you_v3=true&timezone_offset=-360&version=1.6.5".format(i*18,id,state))
            print(page)
            soup = bs(page, "html.parser")
            print(soup)
            output = "{}{}page.json".format(i,state)
            with open(output, 'wb') as f:
                f.write(str(soup).encode())
    
    for i in range(0,20):
        print(i)
        with open('{}{}page.json'.format(i,state), 'r', encoding="utf8") as file:
            data = json.load(file)

        print(data)
        if i == 0:
            print("yo")
            homes = data.get('explore_tabs')[0].get('sections')[0].get('listings')
        else:
            homes = data.get('explore_tabs')[0].get('sections')[0].get('listings')
            print("fo")
        for home in homes:
            obj = {
                "state": "{}".format(state),
                "room_id": "{}".format(str(home.get('listing').get('id'))),
                "name": "{}".format(str(home.get('listing').get('name'))),
                "city": "{}".format(home.get('listing').get('city')),
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
                "price": "{}".format(home.get('pricing_quote').get('rate').get('amount')),
                "lat": "{}".format(home.get('listing').get('lat')),
                "long": "{}".format(home.get('listing').get('lng'))
            }
            data_dict.append(obj)
f = open("sample.csv", "w", encoding='utf-8')
writer = csv.DictWriter(
    f, fieldnames=["state","room_id", "name", "city", "person_cap", "bedrooms", "bathrooms",
    "amenities", "reviews", "prop_type", "guests", "star", "avg_rating", "min_nights",
    "max_nights", "price", "lat", 'long'])
writer.writeheader()
writer.writerows(data_dict)