# Parse json from rest api
import requests
import json

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
json = response.json()
print(json.dumps(json, indent = 2,))

# Get the JSON response and store it as a Python dict
my_dictionary = requests.get(url).json()

# methods
response.content() # Return the raw bytes of the data payload
response.text() # Return a string representation of the data payload
response.json() # This method is convenient when the API returns JSON

# use query to filter data
query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
print(response.json())

# Create a new resource
response = requests.post('https://httpbin.org/post', data = {'key':'value'})
# Update an existing resource
requests.put('https://httpbin.org/put', data = {'key':'value'})

# retrieve metadata
print(response.headers["date"]) 

# Authenticate to rest api, type login to site
requests.get(
  'https://api.github.com/user', 
  auth=HTTPBasicAuth('username', 'password')
)

# or use tokens, more secure
my_headers = {'Authorization' : 'Bearer {access_token}'}
response = requests.get('http://httpbin.org/headers', headers=my_headers)

# use session object
session = requests.Session()
session.headers.update({'Authorization': 'Bearer {access_token}'})
response = session.get('https://httpbin.org/headers')

# check for http errors
# 1xx Informational 2xx Successful 3xx Redirection 4xx Client Error 5xx Server Error 
response = requests.get("http://api.open-notify.org/astros.json")
if (response.status_code == 200):
    print("The request was a success!")
    # Code here will only run if the request is successful
elif (response.status_code == 404:
    print("Result not found!")
    # Code here will react to failed requests
      
# raise an exception
try:
    response = requests.get('http://api.open-notify.org/astros.json', timeout=5)
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)

      
      

