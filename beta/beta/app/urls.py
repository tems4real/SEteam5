"""
Definition of urls for polls viewing and voting.
"""

from django.conf.urls import patterns, url, include
from app.models import Poll
from app.views import PollListView, PollDetailView, PollResultsView
from .views import SignUpView

urlpatterns = patterns('',
    url(r'^$',
        PollListView.as_view(
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='app/index.html',),
        name='home'),
    url(r'^(?P<pk>\d+)/$',
        PollDetailView.as_view(
            template_name='app/details.html'),
        name='detail'),
    url(r'^(?P<pk>\d+)/results/$',
        PollResultsView.as_view(
            template_name='app/results.html'),
        name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'app.views.vote', name='vote'),
    #url(r'^home$', 'home', name='app_home'),
    url(r'^signup$', 
        SignUpView.as_view(
            template_name= 'app/signup.html'), 
        name='signup'),
)
