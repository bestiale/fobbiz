from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from .models import Veranstaltung


class VeranstaltungContent(models.Model):
	veranstaltung = models.ForeignKey(Veranstaltung)

	class Meta():
		abstract = True
		verbose_name = _("Veranstaltung")
		verbose_name_plural = _("Veranstaltungen")

	def render(self, request, context, **kwargs):

		return render_to_string("elephantblog/entry_detail.html",{
			'veranstaltung': self.veranstaltung,
		})
	print veranstaltung