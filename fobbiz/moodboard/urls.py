"""
    filename:       urls.py
    author:         R. Coroneo
    date:           21.05.2013
    description:    Calls the needed view to render the moodboard
"""

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('fobbiz.moodboard.views',
    url(r'^$', 'moodboard', name='moodboard'),
)