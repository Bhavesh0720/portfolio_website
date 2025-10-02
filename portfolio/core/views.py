from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def home(request):
    context = {
        'home':'active',
    }
    return render(request, 'core/home.html', context)


def contact(request):
    context = {'contact': 'active'}

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        full_message = f"Message from {name} ({email}):\n\n{message}"

        try:
            send_mail(
                subject,
                full_message,
                email,  
                [settings.DEFAULT_FROM_EMAIL],  
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        except Exception as e:
            messages.error(request, f"Error sending message: {e}")

    return render(request, 'core/contact.html', context)


def projects(request):
    project_list = [
        {
            'title': 'Footwear Master Ecommerce Site',
            'description': 'An Ecommerce website for purchasing footwears.',
            'technologies': ['Python', 'Django', 'HTML', 'CSS', 'JavaScript', 'Bootstrap'], 
            'link': 'https://bhavesh5433.pythonanywhere.com/',
        },
        {
            'title': 'Grand Hotel Management System',
            'description': 'A hotel management system to manage bookings, rooms, and customer data efficiently.',
            'technologies': ['Python', 'Flask', 'MySQL', 'HTML', 'CSS', 'JavaScript', 'Bootstrap'],
            'report': 'core/doc/grand_hotel.pdf',  # Path to PDF in static folder
        },
        {
            'title': 'Bhumi TV Mart',
            'description': 'A desktop-based retail management system for TV and electronics store, built using Python and Tkinter.',
            'technologies': ['Python', 'Tkinter', 'MySQL'],
            'report': 'core/doc/bhumi_tv_mart.pdf',
        },
        # Add more projects here if needed
    ]
    return render(request, 'core/projects.html', {'projects': project_list, 'active':'active'})