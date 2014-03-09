from mongoengine import *

#connect('life_line', host='troup.mongohq.com', port=10014, username='kerem_is_gay', password='it_is_true')
connect('test')

class User(Document):
    email = StringField(required=True, unique=True)
    name = StringField(max_length=50, required=True)
    password = StringField(required=True)
    birthdate = DateTimeField(required=True)
    gender = StringField(max_length=6)
    smoker = BooleanField()