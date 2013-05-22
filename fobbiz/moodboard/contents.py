#coding=utf-8

"""
    filename:       contents.py
    author:         R. Coroneo
    date:           21.05.2013
    description:    ApplicationContent for the Moodboard
"""
from django.db import models
from django.template.loader import render_to_string

from .models import Moodboard

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