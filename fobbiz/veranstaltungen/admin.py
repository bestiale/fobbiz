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


def excel_export(modeladmin, request, queryset):
    response = HttpResponse(mimetype='text/csv')
    timestamp = now().strftime('%d%m%y_%H%M')
    filename = 'anmeldungen_export_%s.csv' % timestamp
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    writer = csv.writer(response, delimiter=';')

    header = (
        'ANREDE',
        'NAME',
        'VORNAME',
        'E-MAIL',
        'STRASSE',
        'PLZ',
        'ORT',
        'VERANSTALTUNG',
    )

    writer.writerow([row for row in header])

    fields = (
        'anrede',
        'nachname',
        'vorname',
        'e_mail',
        'street_nr',
        'plz',
        'ort',
        'veranstaltung',

    )

    def serialize(obj, field):
        f, attr, value = lookup_field(field, obj, modeladmin)
        value = value if value is not None else ''
        if type(value) == date:
            value = value.strftime('%d.%m.%Y')
        return force_unicode(value).encode('utf-8')

    for obj in queryset:
        writer.writerow([serialize(obj, field) for field in fields] + [''])

    return response

excel_export.short_description = 'Anmeldungen Export (CSV, UTF-8)'


class AnmeldungAdmin(admin.ModelAdmin):

	list_filter = ('veranstaltung',)
	list_display = ('vorname', 'nachname', 'e_mail', 'veranstaltung')
	actions = [excel_export]


admin.site.register(Veranstaltung, VeranstaltungAdmin)
admin.site.register(Anmeldung, AnmeldungAdmin)