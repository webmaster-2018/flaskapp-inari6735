# -*- coding: utf-8 -*-
# quiz-orm/views.py

from flask import Flask
from flask import render_template, request, redirect, url_for, abort, flash
from modele import *
from forms import *

from uczniowie.forms import KlasaForm
from uczniowie.modele import Klasa

app = Flask(__name__)

@app.route('/')
def index():
    """Strona główna"""
    return render_template('index.html')

def get_or_404(kid):
    try:
        k = Klasa.get_by_id(kid)
        return k
    except Klasa.DoesNotExist:
        abort(404)

@app.route("/dodajklase", methods=['GET', 'POST'])
def dodaj():
    """Dodawanie klasy"""
    form = KlasaForm()

    if form.validate_on_submit():
        Klasa(nazwa=form.nazwa.data, roknaboru=form.roknaboru.data, rokmatury=form.rokmatury.data).save()
        return redirect(url_for('lista_klas'))

    return render_template('dodaj_klase.html', form=form)


@app.route("/lista_klas", methods=['GET', 'POST'])
def lista_klas():
    klasy = Klasa.select()

    return render_template('lista_klas.html', klasy=klasy)

@app.route("/lista_klas/<int:kid>", methods=['GET', 'POST'])
def edytuj_klase(kid):
    k = get_or_404(kid)
    form = KlasaForm()
    klasy = Klasa.select()

    if form.validate_on_submit():
        k.nazwa = form.nazwa.data
        k.roknaboru = form.roknaboru.data
        k.rokmatury = form.rokmatury.data
        k.save()
        return redirect(url_for('lista_klas'))

    return render_template('edytuj_klase.html', form=form, iducznia=k, klasy=klasy)

