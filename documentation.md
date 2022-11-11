# NASA APOD API PROJECT
This file contains the documentation for this project.

This project is based on NASA APOD API. For NASA's documentation go to: https://github.com/nasa/apod-api

For quick use:

- pip install -r requirements.txt
- change the params variable in main.py as needed.
- run: python main.py

## Config in get_response.py:
api_key, default=DEMO_KEY. 

To create your own key go to: https://api.nasa.gov/#signUp

The default value has some limitation. For more information go to NASA's website.

mongodb.connection.db_connect() creates the connection with mongodb.

## URL search params and the class Requesting_api in get_response.py:
This project is requesting https://api.nasa.gov/planetary/apod.

The class Requesting_api gets a response from the NASA's apod api and returns it as a list of json. The expected parameters for searching the data are:

- date: 'YYYY-MM-DD', must be between 1995-06-16 and today.

OR

- count: 0 < int <= 100, it returns data from randomly chosen images. The quantity of data returned is = count.

OR

- start_date: 'YYYY-MM-DD', returns data from the range start_date to end_date = today.

OR

- start_date and end_date: 'YYYY-MM-DD', returns data from the range start_date to end_date.

OR

- if params is empty: date = today is returned.

This class checks if the params given are valid. If the params are valid, it returns a list of json. If the params are not valid, it returns an error message.

## Database connection and adding responses
The directory mongodb/ has two files: 

- connection.py: creates a connection with mongodb using default host and port.

- apod.py: creates the collection 'apod' that will keeps the data.

In the get_response.py file, the function save_request() add the response to the database if the request is valid. If the request is not valid, it returns an error message and
does not add it to in the database.

Duplicate dates data is not added to the database.
