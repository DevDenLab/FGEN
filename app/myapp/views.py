from datetime import date
from django.contrib.auth.decorators import login_required
from .forms import ContactForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import Program

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
@login_required
def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save(commit=False)
            if request.user.is_authenticated:
                contact_message.user = request.user
            contact_message.save()

            # Send email to special users
            subject = f"New Contact Form Submission: {contact_message.subject}"
            message = f"Name: {contact_message.name}\nEmail: {contact_message.email}\nMessage: {contact_message.message}"
            print(message)
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = ['tatvajoshi0@gmail.com']  # Add email addresses of special users
            send_mail(subject, message, from_email, recipient_list)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contactus')
    else:
        form = ContactForm()

    return render(request, 'Contactus.html', {'form': form})

def events(request):
    return render(request, 'Events.html', {'active_page': 'events', 'current_year': current_year})

def GetInvolved(request):
    return render(request, 'GetInvolved.html', {'active_page': 'GetInvolved', 'current_year': current_year})

def resources(request):
    return render(request, 'Resources.html', {'active_page': 'resources', 'current_year': current_year})

def programs(request):
    programs = Program.objects.all()
    return render(request, 'Programs.html', {'programs': programs})