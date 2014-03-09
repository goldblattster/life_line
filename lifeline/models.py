from mongoengine import *

connect('life_line', 'mongodb://kerem_is_gay:it_is_true@troup.mongohq.com:10014/life_line')

class User(Document):
    email = StringField(required=True)
    name = StringField(max_length=50)
    password = StringField()