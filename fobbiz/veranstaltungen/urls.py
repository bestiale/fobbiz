from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('fobbiz.veranstaltungen.views',
    #url(r'^$', 'veranstaltung_list', name='veranstaltung_list'),
    url(r'^(?P<slug>[^/]+)/$', 'veranstaltung_detail', name='veranstaltung_detail'),
)