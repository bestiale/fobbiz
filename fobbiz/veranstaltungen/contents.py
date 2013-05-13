from django.db import models
from django.template.loader import render_to_string
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from .models import Veranstaltung
from .forms import AnmeldungForm


class VeranstaltungContent(models.Model):

	veranstaltung = models.ForeignKey(Veranstaltung)

	form = AnmeldungForm

	class Meta():
		abstract = True
		verbose_name = _("Veranstaltung")
		verbose_name_plural = _("Veranstaltungen")

	def render(self, request, context, **kwargs):

		return render_to_string("veranstaltungen/anmelde_form.html",{
			'content' : self,
			'veranstaltung': self.veranstaltung,
			'form': self.form,
			},
			context_instance = RequestContext(request)
			)