from django.shortcuts import render
from datetime import date

 # Get the current date
current_date = date.today()
# Access the year attribute to get the current year
current_year = current_date.year
def index(request):
    return render(request, 'Home.html', {'active_page': 'home','current_year': current_year})

def meeting(request):
    return render(request, 'meetings.html')


def meeting_details(request):
    return render(request, 'meeting-details.html')

def aboutus(request):
    return render(request, 'Aboutus.html', {'active_page': 'about', 'current_year': current_year})

def contactus(request):
    active_page = "contact"
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
    return render(request, 'Contactus.html', {'active_page': 'contact', 'current_year': current_year})

def events(request):
    return render(request, 'Events.html', {'active_page': 'events', 'current_year': current_year})

def GetInvolved(request):
    return render(request, 'GetInvolved.html', {'active_page': 'GetInvolved', 'current_year': current_year})

def resources(request):
    return render(request, 'Resources.html', {'active_page': 'resources', 'current_year': current_year})

def programs(request):
    return render(request,'Programs.html', {'active_page': 'programs', 'current_year': current_year})