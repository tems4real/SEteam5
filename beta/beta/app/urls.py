﻿"""
Definition of urls for polls viewing and voting.
"""
from django.conf.urls import patterns, url, include
from app.models import Poll
from app.views import PollListView, PollDetailView, PollResultsView
from .views import SignUpView

from django.conf.urls import patterns, url
from calendarium.views import (
    CalendariumRedirectView,
    DayView,
    EventCreateView,
    EventDeleteView,
    EventDetailView,
    EventUpdateView,
    MonthView,
    OccurrenceDeleteView,
    OccurrenceDetailView,
    OccurrenceUpdateView,
    UpcomingEventsAjaxView,
    WeekView,
)
urlpatterns = patterns('',
    # event views
    url(r'^event/create/$',
        EventCreateView.as_view(),
        name='calendar_event_create'),

    url(r'^event/(?P<pk>\d+)/$',
        EventDetailView.as_view(),
        name='calendar_event_detail'),

    url(r'^event/(?P<pk>\d+)/update/$',
        EventUpdateView.as_view(),
        name='calendar_event_update'),

    url(r'^event/(?P<pk>\d+)/delete/$',
        EventDeleteView.as_view(),
        name='calendar_event_delete'),

    # occurrence views
    url(r'^event/(?P<pk>\d+)/date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$',
        OccurrenceDetailView.as_view(),
        name='calendar_occurrence_detail'),

    url(
        r'^event/(?P<pk>\d+)/date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/update/$',  # NOPEP8
        OccurrenceUpdateView.as_view(),
        name='calendar_occurrence_update'),

    url(
        r'^event/(?P<pk>\d+)/date/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/delete/$',  # NOPEP8
        OccurrenceDeleteView.as_view(),
        name='calendar_occurrence_delete'),
    # calendar views
    url(r'^(?P<year>\d+)/(?P<month>\d+)/$',
        MonthView.as_view(),
        name='calendar_month'),

    url(r'^(?P<year>\d+)/week/(?P<week>\d+)/$',
        WeekView.as_view(),
        name='calendar_week'),

    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$',
        DayView.as_view(),
        name='calendar_day'),

    url(r'^get-events/$',
        UpcomingEventsAjaxView.as_view(),
        name='calendar_upcoming_events'),

    url(r'^$',
        CalendariumRedirectView.as_view(),
        name='calendar_current_month'),
    url(r'^calendar/', include('calendarium.urls')),
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
