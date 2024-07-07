from django.shortcuts import render

def index(request):
    return render(request, 'Home.html')

def meeting(request):
    return render(request, 'meetings.html')


def meeting_details(request):
    return render(request, 'meeting-details.html')

def aboutus(request):
    return render(request, 'Aboutus.html')