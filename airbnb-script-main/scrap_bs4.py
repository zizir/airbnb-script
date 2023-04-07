import requests
from bs4 import BeautifulSoup

# Specify the URL of the Airbnb search results page you want to scrape
url = 'https://www.airbnb.com/s/Paris--France/homes?refinement_paths%5B%5D=%2Fhomes&search_type=filter_change&tab_id=home_tab&query=Paris%2C%20France&place_id=ChIJD7fiBh9u5kcRYJSMaMOCCwQ&checkin=2023-03-01&checkout=2023-03-05&adults=1&source=structured_search_input_header&search_type=autocomplete_click'

# Send an HTTP request to the specified URL and get the HTML content
response = requests.get(url)
html_content = response.content

# Create a BeautifulSoup object and specify the HTML parser
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the property listings on the search results page
listings = soup.find_all('div', class_='_8s3ctt')

print(soup)
# Loop through each listing and extract the desired information
for listing in listings:
    print("DEBUG")
    # Extract the property name
    name = listing.find('div', class_='_bzh5lkq').text.strip()
    
    # Extract the property price per night
    price = listing.find('span', class_='_krjbj').text.strip()
    
    # Extract the property rating
    rating = listing.find('span', class_='_10fy1f8').text.strip()
    
    # Print the extracted information
    print('Name:', name)
    print('Price per night:', price)
    print('Rating:', rating)
    print('------------------')
