# encoding: utf-8

from django.db import models
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify

class Veranstaltung(models.Model):

	titel = models.CharField(_('title'), max_length=100)
	slug = models.SlugField(_('slug'), unique=True)
	#image = models.ImageField(_('image'),
		#upload_to="veranstaltungen/")
	#beschreibung = models.TextField(_('description'))
	datum = models.DateTimeField(_('date'), blank=True)
	plaetze = models.IntegerField(_('place'), blank=True, null=True)
	#is_active = models.BooleanField(_('is active'), default=True)
	#erfasst = models.DateTimeField(_('add'), auto_now_add=True)
	#aktualisiert = models.DateTimeField(_('update'), auto_now=True)


	class Meta:
		verbose_name = u'Veranstaltung'
		verbose_name_plural = u'Veranstaltungen'

	def __unicode__(self):
		return self.titel

	@models.permalink
	def get_absolute_url(self):
		return ('veranstaltung_detail', (), {'slug': self.slug})


class Anmeldung(models.Model):

	ANREDE_CHOICES = (
		('w', u'Frau'),
		('m', u'Herr'),
	)

	veranstaltung = models.ForeignKey(Veranstaltung, related_name='veranstaltung')
	anrede = models.CharField(_('anrede'), choices=ANREDE_CHOICES, max_length=1)
	vorname = models.CharField(_('first name'), max_length=100)
	nachname = models.CharField(_('last name'), max_length=100)
	e_mail = models.EmailField(_('e-mail'), max_length=254)
	street_nr = models.CharField(_('adresse'), max_length=200)
	plz = models.IntegerField(_('zip'))
	ort = models.CharField(_('city'), max_length=100)

	class Meta:
		verbose_name = u'Anmeldung'
		verbose_name_plural = u'Anmeldungen'

	def __unicode__(self):
		return self.e_mail

