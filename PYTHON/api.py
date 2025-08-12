"""
API stands for "Application Programming Interface." 
In simple terms, it's a set of rules and protocols that allow how different software applications can communicate and interact with each other. 
APIs define the methods and data formats that applications can use to request and exchange information. To retrieve data from a web server, a client application initiates a request, 
and the server responds with the requested data.

APIs act as bridges that enable the smooth exchange of data and functionality, enhancing interoperability across various applications. 
Let's learn about how to work with APIs in Python

Making API Requests in Python
In order to work with APIs, some tools are required, such as requests module and we need to first install them in our system.

Command to install 'requests':

pip install requests

Once we have installed it, we need to import it in our code to use it.

Command to import 'requests':

import requests

Let us understand the working of API with examples. First let us take a simple example.


"""

import requests

"""
Example 1: Fetching Live Stock Price
This example retrieves the latest opening price for IBM stock at a 5-minute interval from alphavantage api endpoint. 
Here we are using 'requests' to make a call and it is checked with the help of status code that whether our request was successful or not. 
Then the response is converted to python dictionary and the respected data is stored.

"""
def get_Stock_data():
    url="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&outputsize=full&apikey=demo"
    response=requests.get(url)
    if response.status_code==200:
        data=response.json()
        
        last_refreshed=data["Meta Data"]["3. Last Refreshed"]
        price=data["Time Series (5min)"][last_refreshed]["1. open"]
        return price
    else:
        return None
price=get_Stock_data()
symbol="IBM"
if price is not None:
    print(f"{symbol}: {price}")
else:
    print("Failed to retrieve data.")

# Explanation:

# Sends a GET request to Alpha Vantage API.
# Checks if the request was successful (status_code == 200).
# Parses JSON response to extract latest opening stock price.
# Prints the price or error message.

"""
Understanding API Status Codes
Status codes tell us how the server handled our request:

--> 200 OK: Request successful, data returned.
--> 201 Created: New resource created.
--> 204 No Content: Success but no data returned.
--> 400 Bad Request: Invalid request.
--> 401 Unauthorized: Missing or invalid API key.
--> 500 Internal Server Error: Server encountered an error.
These codes help in debugging and managing API responses.

"""

"""
Example 2: Fetching News Headlines Using NewsAPI
To fetch news, you often need an API key for authentication. 
Here’s how to get top business headlines from the US.

"""
import requests

API_KEY = 'your_api_key_here'
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=%7BAPI_KEY%7D"
response = requests.get(url)
print(response.status_code)

# Builds a URL with parameters including API key.
# Sends GET request to NewsAPI.
# Prints status code to confirm request success (200 means OK).

"""
Working with JSON Data
When working with APIs, understanding JSON is key because it’s the common format APIs use to send data. 
Think of JSON as the language APIs speak to share information like news headlines, images, and descriptions.

To handle this data, we use Python and the requests library to fetch news from NewsAPI. 
Then, Python helps organize and display the top articles clearly- like a helpful librarian sorting through lots of information for us. 
This shows how JSON and Python work together to make API data easy to use.

"""

import json


def fetch_and_print_articles(api_url):
    response = requests.get(api_url)
    
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        
        for index, article in enumerate(articles[:1], start=1):
            print(f"Article {index}:\n{json.dumps(article, sort_keys=True, indent=4)}\n")
    else:
        print(f"Error: {response.status_code}")

API_KEY = '7748f3ce8f1946078a641537c17a5f4d'
api_endpoint = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"

fetch_and_print_articles(api_endpoint)

def jprint(obj):
    print(json.dumps(obj, sort_keys=True, indent=4))



# Parses JSON from the API response.
# enumerate(articles[:1], start=1) prints details of top 1 news article formatted neatly.
# Handles errors by checking response status.


"""
Using Query Parameters in API Requests
When using an API like NewsAPI, it’s important to specify exactly what data you want. 
In this example, we fetch the top headlines for the United States. We use the API’s URL (API_URL) and provide our unique API key (API_KEY) for access.

But having just the URL and key isn’t enough. APIs let you customize your request with parameters. 
Here, we use a params dictionary to set the country to "us" and include our API key to authenticate the request."""

params = {
    "country": "us",
    "apiKey": API_KEY,
    "pageSize": 1
}

response = requests.get(api_endpoint, params=params)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}")

# Defines parameters as a dictionary.
# Passes parameters in the requests.get() call.
# Prints JSON response or error status.
# "pageSize": 1 in params{...} ensure that only 1 headline get fetched (you can modify it accordingly)

"""
Example 3: Tracking the International Space Station (ISS) Location
This example uses several libraries to track ISS in real-time and map its position using Python’s turtle graphics.

Key libraries used:
--> json: For decoding JSON data from API.
--> turtle: For graphical map display.
--> urllib.request: To fetch API data.
--> time: For periodic updates.
--> webbrowser: To open files.
--> geocoder: To find current user location.


Step 1: Fetch Current Astronauts Data
So now there is a problem with tracking ISS because it travels at a speed of almost 28000km/h. Thus, it takes only 90 minutes to complete 1 rotation around the earth. At such a speed, it becomes quite difficult to lock the exact coordinates. So here comes the API to solve this issue. API acts as an intermediate between the website and the program, thus providing the current time data for the program.

In our case, API will provide us with the current location of ISS in earth’s orbit, so visit the link below as an API link for astronaut info.

url = "http://api.open-notify.org/astros.json" 

Accessing Data
Use urllib.request.urlopen() function inorder to open the API url and json.loads(.read()) function to read the data from the URL.

"""


import urllib.request

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
print("\n\n\n",result)

# Opens API URL and reads JSON data.
# Prints astronauts currently in space.

"""
Step 2: Save Astronauts Info to File
Create iss.text file using an open() function in write mode and write the result (names & numbers of astronauts) as data inside the file.

"""
file = open("iss.txt", "w")
file.write(f"There are currently {result['number']} astronauts on the ISS:\n\n")

for person in result["people"]:
    file.write(person['name'] + " - onboard\n")

file.close()


'''
Step 3: Get User's Current Location
Use geocoder.ip(‘me’) to know your current location in terms of latitude and longitude.

'''
import geocoder

g = geocoder.ip('me')
print(f"Your current location: {g.latlng}")


'''
Step 4: Setup ISS Tracking Map (with Turtle)
Use turtle.screen() function to get access to the screen, then use screen.setup() to set the size and position of the output window. 
Use screen.setworldcoordinates() function to set the coordinates of all 4 corners on x, y-axis so that when iss reach out from reaches they appear again from another edge.

'''
import turtle

screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

screen.bgpic("images/map.gif")
screen.register_shape("images/iss.gif")

iss = turtle.Turtle()
iss.shape("images/iss.gif")
iss.setheading(45)
iss.penup()