# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, FieldList, IntegerField
from wtforms import SelectField, FormField, BooleanField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'


class KlasaForm(FlaskForm):
    id = HiddenField()
    nazwa = StringField()
    roknaboru = IntegerField()
    rokmatury = IntegerField()
    


class UczenForm(FlaskForm):
    id = HiddenField()
    imie = StringField('Imie: ')
    nazwisko = StringField('Nazwisko: ')
    plec = BooleanField('Płeć: ')
    klasa = SelectField('Klasa', coerce=int)
