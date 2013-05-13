# encoding: utf-8
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail

from .models import Veranstaltung
from .forms import AnmeldungForm


def save_anmeldung(request):


    if request.method == 'POST':
        veranstaltung = get_object_or_404(Veranstaltung, slug=request.POST['slug'])
        form = AnmeldungForm(request.POST)
        if form.is_valid():
            anmeldung = form.save(commit=False)
            anmeldung.veranstaltung = veranstaltung
            anmeldung.save()
            send_infomail(veranstaltung)
            if veranstaltung.plaetze >= 0:
                veranstaltung.plaetze = veranstaltung.plaetze - 1
                veranstaltung.save()
            return redirect(request.POST['path'])
    else:
        form = AnmeldungForm()
    return render(request, 'veranstaltungen/anmelde_form.html',{
    	'form': form,
	})

def send_infomail(veranstaltung):

    subject = "Neue Anmeldung für %s" % veranstaltung
    message =   """
                Es ist eine neue Anmeldung für diese Veranstaltung vorhanden.
                Bitte loggen Sie sich im Adminbereich ein um diese Anzusehen
                """
    sender = "fobbiz.ch"

    recipients = [u'rc@feinheit.ch']

    send_mail(subject, message, sender, recipients)
