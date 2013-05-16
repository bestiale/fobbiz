# encoding: utf-8

from django.forms import ModelForm

from .models import Anmeldung

class AnmeldungForm(ModelForm):

	class Meta:
		model = Anmeldung
		exclude = ('veranstaltung',)
