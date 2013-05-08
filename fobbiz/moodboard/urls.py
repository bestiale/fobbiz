from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('fobbiz.moodboard.views',
    url(r'^$', 'moodboard', name='moodboard'),
)