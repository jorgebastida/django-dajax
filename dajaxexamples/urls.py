from django.conf.urls.defaults import *
from django.conf import settings

from dajaxice.core import dajaxice_autodiscover

dajaxice_autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',)

urlpatterns += patterns('',
    # Example:
    # (r'^dajaxTest/', include('dajaxTest.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
	
	#Dajax URLS
	(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
	
	#Website Examples
	(r'^multiply/?$','dajaxexamples.examples.views.multiply'),
	(r'^maps/?$','dajaxexamples.examples.views.maps'),
	(r'random/?$','dajaxexamples.examples.views.random_example'),
	(r'forms/?$','dajaxexamples.examples.views.form_example'),
	(r'pagination/?$','dajaxexamples.examples.views.pagination_example'),
	(r'full_form/?$','dajaxexamples.examples.views.full_form_example'),
	(r'flickr/?$','dajaxexamples.examples.views.flickr_example'),
	
	#Api examples
	(r'apiexamples/?$','dajaxexamples.apiexamples.views.api_examples'),
	(r'.*', 'dajaxexamples.examples.views.index'),
)
