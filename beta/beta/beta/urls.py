"""
Definition of urls for beta.
"""

from django.views.generic import TemplateView
from datetime import datetime
from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.forms import BootstrapAuthenticationForm

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('app.urls', namespace="app")),
    url(r'^contact$', 'app.views.contact', name='contact'),
    url(r'^about', 'app.views.about', name='about'),
    url(r'^seed', 'app.views.seed', name='seed'),
    url(r'^', include('schedule.urls')),
    url(r'^login/$',
        'django.contrib.auth.views.login',
        {
            'template_name': 'app/login.html',
            'authentication_form': BootstrapAuthenticationForm,
            'extra_context':
            {
                'title':'Log in',
                'year':datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        'django.contrib.auth.views.logout',
        {
            'next_page': '/',
        },
        name='logout'),
    url(r'^fullcalendar/', TemplateView.as_view(template_name="app/fullcalendar.html"), name='fullcalendar'),
    url(r'^schedule/', include('schedule.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
