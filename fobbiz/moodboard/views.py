"""
    filename:       views.py
    author:         R. Coroneo
    date:           21.05.2013
    description:    returns moodboards to template "moodboard.html"
"""

from django.shortcuts import get_object_or_404
from .models import Moodboard

def moodboard(request):
    return 'moodboard/moodboard.html', {'object_list': Moodboard.objects.all()}