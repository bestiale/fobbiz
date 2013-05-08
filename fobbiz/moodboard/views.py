from django.shortcuts import get_object_or_404
from .models import Moodboard

def moodboard(request):
    return 'moodboard/moodboard.html', {'object_list': Moodboard.objects.all()}