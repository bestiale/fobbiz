# encoding: utf-8
import csv

from datetime import date

from django.contrib import admin
from django.contrib.admin.util import lookup_field
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


from .models import Veranstaltung, Anmeldung

class VeranstaltungAdmin(admin.ModelAdmin):
	pass

class AnmeldungAdmin(admin.ModelAdmin):
	list_display = ('vorname', 'nachname', 'e_mail', 'veranstaltung')


admin.site.register(Veranstaltung, VeranstaltungAdmin)
admin.site.register(Anmeldung, AnmeldungAdmin)