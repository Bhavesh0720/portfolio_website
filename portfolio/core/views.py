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
                settings.DEFAULT_FROM_EMAIL,  # sender
                [settings.DEFAULT_FROM_EMAIL],  # receiver (your email)
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
            'description': 'Built a full-stack ecommerce application for online footwear shopping with a user-friendly and responsive interface. Implemented product listings, category filtering, cart functionality, secure checkout, user authentication, and order management to provide a seamless shopping experience.',
            'technologies': ['Python', 'Django', 'HTML', 'CSS', 'JavaScript', 'Bootstrap'],
            'link': 'https://bhavesh5433.pythonanywhere.com/',
        },
        {
            'title': 'Blogora Site',
            'description': 'Designed and developed a full-stack blogging platform that enables users to create, manage, and explore blog content through a clean and responsive interface. Implemented user authentication, category-based content organization, blog management features, and an admin dashboard for efficient content moderation.',
            'technologies': ['Python', 'Django', 'HTML5', 'CSS3', 'Bootstrap5'],
            'link': 'https://blogora.pythonanywhere.com/',
        },
        {
            'title': 'Grand Hotel Management System',
            'description': 'Developed a hotel management system to streamline room bookings, customer check-in/check-out, and reservation handling. Implemented room availability tracking, billing management, customer record storage, and an administrative dashboard to improve operational efficiency and reduce manual workload.',
            'technologies': ['Python', 'Flask', 'MySQL', 'HTML', 'CSS', 'JavaScript', 'Bootstrap'],
            'report': 'core/doc/sem5_photos.pdf',
        },
        {
            'title': 'Bhumi TV Mart',
            'description': 'Engineered a desktop-based retail management system for an electronics store to simplify inventory tracking, customer management, billing, and sales monitoring. Built with a user-friendly GUI, the system improves daily retail operations through efficient data handling and streamlined reporting.',
            'technologies': ['Python', 'Tkinter', 'MySQL'],
            'report': 'core/doc/sem6_photos.pdf',
        },
    ]
    return render(request, 'core/projects.html', {'projects': project_list, 'active':'active'})