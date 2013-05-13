from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('fobbiz.veranstaltungen.views',
    # url(r'^(?P<slug>[^/]+)/$', 'veranstaltung_detail',
    # 	name='veranstaltung_detail'),
	url(r'^anmeldung/$', 'save_anmeldung',
		name = 'save_anmeldung'),
)