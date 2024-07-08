from django.shortcuts import render

def index(request):
    return render(request, 'Home.html')

def meeting(request):
    return render(request, 'meetings.html')


def meeting_details(request):
    return render(request, 'meeting-details.html')

def aboutus(request):
    return render(request, 'Aboutus.html')

def contactus(request):
    flag = 0
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
    return render(request, 'Contactus.html')