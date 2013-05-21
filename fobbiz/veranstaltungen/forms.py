# encoding: utf-8

"""
    filename:       forms.py
    author:         R. Coroneo
    date:           21.05.2013
    description:    Generation of "Anmelde Formular" excluding ForeignKey
"""

from django.forms import ModelForm

from .models import Anmeldung

class AnmeldungForm(ModelForm):

	class Meta:
		model = Anmeldung
		exclude = ('veranstaltung',)
