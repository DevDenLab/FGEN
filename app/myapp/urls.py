from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meetings', views.meeting, name='meeting'),
    path('meetingsdetails', views.meeting_details, name='meeting_details'),
    path('about', views.aboutus, name='aboutus'),
    path('contact', views.contactus, name='contactus'),
    path('events', views.events, name='events'),
    path('getinvolved', views.GetInvolved, name='GetInvolved'),
    path('resources', views.resources, name='resources'),
    path('programs', views.programs, name='programs'),
]
