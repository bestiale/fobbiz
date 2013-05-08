from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string

from .models import Veranstaltung
from .forms import AnmeldungForm

# def veranstaltung_list(request):
#     return render(request, 'veranstaltungen/veranstaltung_list.html', {
#     'object_list': Veranstaltung.objects.all(),
# })

def veranstaltung_detail(request, slug):
	form = AnmeldungForm

	return render(request, 'veranstaltungen/veranstaltung_detail.html', {
	    'veranstaltung': get_object_or_404(Veranstaltung, slug=slug),
	    'form' : form,
	})