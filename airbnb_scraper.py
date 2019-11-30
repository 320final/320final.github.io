from bs4 import BeautifulSoup as bs
import requests
import urllib

url = "https://www.airbnb.com/api/v2/explore_tabs?_format=for_explore_search_web&auto_ib=false&client_session_id=12c460bd-4911-4462-855f-dca1778fd776&currency=USD&current_tab_id=home_tab&experiences_per_grid=20&fetch_filters=true&guidebooks_per_grid=20&has_zero_guest_treatment=true&hide_dates_and_guests_filters=false&is_guided_search=true&is_new_cards_experiment=true&is_standard_search=true&items_per_grid=18&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=en&metadata_only=false&query=New%20York%2C%20NY%2C%20United%20States&query_understanding_enabled=true&refinement_paths%5B%5D=%2Fhomes&satori_version=1.1.14&screen_height=969&screen_size=medium&screen_width=1114&selected_tab_id=home_tab&show_groupings=true&supports_for_you_v3=true&timezone_offset=-360&version=1.6.5"

response = requests.get(url)
print(response)
page = urllib.request.urlopen(url)
print(page)
soup = bs(page, "html.parser")
print(soup)

output = "firstpage.json"
with open(output, 'wb') as f:
    f.write(str(soup).encode())
