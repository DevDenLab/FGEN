from django.shortcuts import render

def index(request):
    return render(request, 'Home.html', {'active_page': 'home'})

def meeting(request):
    return render(request, 'meetings.html')


def meeting_details(request):
    return render(request, 'meeting-details.html')

def aboutus(request):
    return render(request, 'Aboutus.html', {'active_page': 'about'})

def contactus(request):
    active_page = "contact"
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
    return render(request, 'Contactus.html', {'active_page': 'contact'})

def events(request):
    return render(request, 'Events.html', {'active_page': 'events'})

def GetInvolved(request):
    return render(request, 'GetInvolved.html', {'active_page': 'GetInvolved'})

def resources(request):
    return render(request, 'Resources.html', {'active_page': 'resources'})

def programs(request):
    return render(request,'Programs.html', {'active_page': 'programs'})