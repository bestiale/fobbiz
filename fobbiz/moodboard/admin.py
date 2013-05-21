#coding=utf-8

"""
    filename:       admin.py
    author:         R. Coroneo
    date:           21.05.2013
    description:    Admin Settings for Moodboard.
"""
from django.contrib import admin
from models import *

class MoodboardAdmin(admin.ModelAdmin):
    list_display = ['title', 'teaser_image',]

admin.site.register(Moodboard, MoodboardAdmin)