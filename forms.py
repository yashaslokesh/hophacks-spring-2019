# from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField

class ClubSearchForm(Form):
    # choices = [('Name', 'name'),
    #            ('URL', 'url'),
    #            ('Description', 'descr')]
    # select = SelectField('Search for clubs:', choices=choices)
    search = StringField('')