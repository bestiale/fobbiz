#coding=utf-8
from django.contrib import admin
from models import *

class MoodboardAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title', 'teaser_text']

admin.site.register(Moodboard, MoodboardAdmin)