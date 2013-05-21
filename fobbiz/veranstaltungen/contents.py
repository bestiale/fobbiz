# encoding: utf-8

"""
    filename:       contents.py
    author:         R. Coroneo
    date:           21.05.2013
    description:    Rendering of the registration form, saving the incoming
    				Data from form, checking with sessions if registration
    				already exists in current session with the incoming mail and
    				event slug
"""

from django.db import models
from django.template.loader import render_to_string
from django.template import RequestContext
from django.shortcuts import get_object_or_404, redirect
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail

from .models import Veranstaltung, Anmeldung
from .forms import AnmeldungForm


class VeranstaltungContent(models.Model):

	veranstaltung = models.ForeignKey(Veranstaltung)

	class Meta():
		abstract = True
		verbose_name = _("Veranstaltung")
		verbose_name_plural = _("Veranstaltungen")

	def render(self, request, context, **kwargs):
		
		if request.method == 'POST':
			veranstaltung = get_object_or_404(Veranstaltung, slug=request.POST['slug'])

			form = AnmeldungForm(request.POST)
			if form.is_valid():				
				if request.session.get('veranstaltung') == request.POST['slug'] and	request.session.get('email') == request.POST['e_mail']:
					return render_to_string("veranstaltungen/already_registered.html",{
								'content': self,
					})
				else:
					anmeldung = form.save(commit=False)
					anmeldung.veranstaltung = veranstaltung
					anmeldung.save()
					request.session['veranstaltung'] = request.POST['slug']
					request.session['email'] = request.POST['e_mail']
					self.send_infomail(veranstaltung)
					if veranstaltung.plaetze >= 0:
					    veranstaltung.plaetze = veranstaltung.plaetze - 1
					    veranstaltung.save()
					return render_to_string("veranstaltungen/thanks.html",{
							'content': self,
					})
		else:
		    form = AnmeldungForm()
		return render_to_string("veranstaltungen/anmelde_form.html",{
			'content' : self,
			'veranstaltung': self.veranstaltung,
			'form': form,
			},
			context_instance = RequestContext(request)
		)

	def send_infomail(request, veranstaltung):

	    subject = u'Neue Anmeldung für %s' % veranstaltung
	    message =   """
	                Es ist eine neue Anmeldung für diese Veranstaltung vorhanden.
	                Bitte loggen Sie sich im Adminbereich ein um diese Anzusehen
	                """
	    sender = "fobbiz.ch"

	    recipients = [u'rc@feinheit.ch']

	    send_mail(subject, message, sender, recipients)
