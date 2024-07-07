from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def meeting(request):
    return render(request, 'meetings.html')
