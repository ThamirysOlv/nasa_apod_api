import mongoengine as mg

''' Creating connection with the database '''

''' data is using a default host and port '''
data = dict(
    host='127.0.0.1',
    port=27017
)

def db_connect():
    mg.register_connection(alias='main', name='NASA_apod_api', **data)

def db_disconnect():
    mg.disconnect('main')