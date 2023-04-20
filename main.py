''' 
Connecting to the nasa apod api - astronomy picture of the day
For documentation go to documentation.md
'''

''' Importing class that requests the API and function that save data to mongodb '''
from get_response import Requesting_api, save_request
from mongodb.apod import Apod

params={
    # Params dates pattern: 'YYYY-MM-DD'
    # Params count pattern: 0 < int <= 100
    'date': None,
    'count': None,
    'start_date': '2022-10-03', 
    'end_date': '2022-10-08'
}
import mongodb.connection
#print(Apod.objects(date='2022-11-11').all())
mongodb.connection.db_connect()

save_request(Requesting_api(**params).list_json_response())