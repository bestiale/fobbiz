# encoding: utf-8

from django.forms import ModelForm

from .models import Anmeldung

class AnmeldungForm(ModelForm):

	class Meta:
		model = Anmeldung
		exclude = ('veranstaltung',)

	def save(self, *args, **kwargs):
        # Dont' save if an exact copy already exist
		try:
		    return Anmeldung.objects.get(**self.cleaned_data)
		except Anmeldung.DoesNotExist:
		    return super(AnmeldungForm, self).save(*args, **kwargs)