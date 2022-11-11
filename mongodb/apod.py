import mongoengine as mg

''' Creating the colletion '''

class Apod(mg.Document):
    #_id = mg.ObjectIdField()
    date = mg.DateField()
    resource = mg.StringField()
    title = mg.StringField()
    url = mg.StringField()
    hdurl = mg.StringField()
    media_type = mg.StringField()
    explanation = mg.StringField()
    thumbnail_url = mg.StringField()
    copyrights = mg.StringField()
    service_version = mg.StringField()

    meta = {'db_alias': 'main', 'collection': 'apod'}