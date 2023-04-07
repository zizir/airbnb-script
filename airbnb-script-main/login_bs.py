import requests
from bs4 import BeautifulSoup
from selenium import webdriver
DEBUG = True

# Send a GET request to the Airbnb login page to obtain the CSRF token
login_url = 'https://www.airbnb.com/login'
response = requests.get(login_url)
soup = BeautifulSoup(response.content, 'html.parser')

# aria-label="Continue with email"
email_btn = soup.find("button", {"aria-label": "Continue with email"})
if DEBUG:
    print(email_btn)


onclick = email_btn.get('onclick')
if DEBUG:
    print(onclick)



if response.ok:
    print('Button clicked')
else:
    print('Failed to click button')

# csrf_token = soup.find('input', {'name': '_csrf_token'})['value']

# # Send a POST request to the Airbnb login endpoint with the login credentials and CSRF token
# login_data = {
#     'email': 'your_email_address',
#     'password': 'your_password',
#     '_csrf_token': csrf_token
# }
# response = requests.post(login_url, data=login_data)

# # Check if the login was successful
# if response.ok:
#     # Extract the session cookie from the response headers
#     session_cookie = response.cookies.get('airbnb_session')
#     print('Login successful')
# else:
#     print('Login failed')
