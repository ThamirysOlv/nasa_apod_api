''' 
Connecting to the nasa apod api - astronomy picture of the day
For documentation go to documentation.md
'''

import requests
from decouple import config
import mongoengine as mg

'''
Importing libraries
    - requests    : send HTTP requests
    - decouple    : deal with environment variables
    - mongoengine : connect python and mongodb      
'''

''' Importing connection with the database and the collection apod'''
import mongodb.connection
from mongodb.apod import Apod

''' Config '''
api_key = config('PERSONAL_API_KEY', default='DEMO_KEY')
api_url = 'https://api.nasa.gov/planetary/apod'
mongodb.connection.db_connect()

''' Classes '''
class Requesting_api:
    ''' 
    Requesting_api get a response from the api_url with the expected params 
    and returns a list of json
    
    Expected params are:
        - date: 'YYYY-MM-DD', must be between 1995-06-16 and today.
        OR
        - count: 0 < int < 100, it returns randomly chosen images.
        OR
        - start_date: 'YYYY-MM-DD', returns data from the range start_date to end_date = today
        OR
        - start_date and end_date: 'YYYY-MM-DD', returns data from the range start_date to end_date
        OR
        - if params is empty: date = today is returned.
    '''

    def __init__(self, api_key=api_key, date=None, count=None, start_date=None, end_date=None):
        self.api_key = api_key
        self.date = date
        self.count = count
        self.start_date = start_date
        self.end_date = end_date

    # private method: only accessible inside the class.
    def __get_apod_api(self):
        ''' Getting response from the API'''
        params = {'api_key': self.api_key, 'date': self.date, 'start_date': self.start_date, 
                    'end_date': self.end_date, 'count': self.count}
        response = requests.get(api_url, params=params, timeout=100)
        return response

    # private method: only accessible inside the class.
    def __check_response_status_code(self):
        ''' Checking if response is valid'''

        if self.__get_apod_api().status_code == 200:
            return True
        elif self.__get_apod_api().status_code == 404:
            return f'Error {self.__get_apod_api().status_code}: Data not found. Try again with different params.'
        elif self.__get_apod_api().status_code == 400:
            return f'Error {self.__get_apod_api().status_code}: Bad request. Check params options and/or ranges.'
        else:
            return f'Error {self.__get_apod_api().status_code}'
    
    def list_json_response(self):
        ''' This method format response to a list of json if response is valid.
        If the request is not valid, it returns a error message.
        
        When params=count or params=start_date or params=start_date and end_date, 
        the response is a list of dict. However, when params=date, the response is one dict.

        This method append dict to a list when params=date,
        so we have an uniform return of list of json data.
        '''
        l=[]
        if self.__check_response_status_code() == True:
            if self.date !=None or (self.date==None and self.count==None and self.start_date==None and self.end_date==None):
                l.append(self.__get_apod_api().json())
                return l
            else:
                return self.__get_apod_api().json()
        else:
            return self.__check_response_status_code()

def save_request(your_request):
    ''' save_resquest save the output of Requesting_api (your_request) in the db if the request is valid. 
    If the request is not valid, it returns an error message and the data is not saved in the db. 
    
    The function is getting each item in the list returned by Requesting_api.
    The method get() is checking if the specific key exists in the json,
    if it does not exist it returns 'None', if it does exist it returns the key's value.
    After that, the data for each picture is saved in the database.
    '''
    if type(your_request) is str:
        print(your_request)
    else:
        for item in your_request:
            Apod(date=item.get('date'), resource=item.get('resource'), title=item.get('title'), url=item.get('url'), hdurl=item.get('hdurl'), 
                    media_type=item.get('media_type'), explanation=item.get('explanation'), thumbnail_url=item.get('thumbnail_url'), 
                    copyrights=item.get('copyright'), service_version=item.get('service_version')).save()

# CREATE CODE FOR CHECKING IF DATE ALREADY EXISTS IN THE DATABASE

#print(your_request[0].get('date'))
params={
    # Params dates pattern: 'YYYY-MM-DD'
    # Params count pattern: 0 < int <= 100
    'date': None,
    'count': None,
    'start_date': None, 
    'end_date': None
}

#print(Requesting_api(**params).list_json_response())
save_request(Requesting_api(**params).list_json_response())
#print(Requesting_api().list_json_response()[0]['copyright'])
#test = Apod(date='2022-10-11').save()