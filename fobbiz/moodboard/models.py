#coding=utf-8

"""
    filename:       models.py
    author:         R. Coroneo
    date:           21.05.2013
    description:    Needed models for moodboard inclusive applicationcontent.
"""

from django.utils.translation import ugettext_lazy as _
from django.db import models

from feincms.module.medialibrary.models import MediaFile

# Moodboard Model

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