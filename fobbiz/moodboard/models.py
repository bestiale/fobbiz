from django.db import models
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from feincms.module.medialibrary.models import MediaFile


class Moodboard(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    teaser_text = models.TextField(_('teaser text'), blank=True)
    teaser_image = models.ForeignKey(MediaFile, related_name='moodboard_teasers')

    link_text = models.CharField(_('link text'), max_length=255, blank=True)
    link = models.CharField(_('link'), max_length=255, blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('moodboard')


class ShowMoodboard(models.Model):
    class Meta():
        abstract = True

    def render(self, request, context, **kwargs):

        moodboards = Moodboard.objects.all()

        if moodboards:

            return render_to_string("moodboard/moodboard.html", {
                'moodboard_list': moodboards,
                }, context_instance = context,
            )
