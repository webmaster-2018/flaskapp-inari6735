# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, IntegerField
from wtforms.validators import DataRequired

blad1 = 'To pole jest wymagane'


class KlasaForm(FlaskForm):
    id = HiddenField()
    nazwa = StringField('Nazwa klasy:', validators=[DataRequired(message=blad1)])
    roknaboru = IntegerField('Rok naboru:', validators=[DataRequired(message=blad1)])
    rokmatury = IntegerField('Rok matury:', validators=[DataRequired(message=blad1)])
