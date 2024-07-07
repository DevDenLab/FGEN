from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('meetings', views.meeting, name='meeting'),
    path('meetingsdetails', views.meeting_details, name='meeting_details'),
    path('about', views.aboutus, name='aboutus')
    
]
