from django.shortcuts import render, redirect
from .models import Usermodel, Projectmodel, Comment
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import get_object_or_404



# HOME
def home(request):
    users = Usermodel.objects.all()

    return render(
        request,
        'civilengineering/index.html',
        {'User': users}
    )


# ALL PROJECTS
# ALL PROJECTS + SEARCH + COMMENTS
def project(request):

    query = request.GET.get('q')

    projects = Projectmodel.objects.all().order_by('-created_at')

    if query:
        projects = projects.filter(title__icontains=query)

    # ⭐ HANDLE COMMENT POST
    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')

        if name and message:
            Comment.objects.create(
                name=name,
                message=message
            )

        return redirect('project')  # VERY IMPORTANT

    comments = Comment.objects.all().order_by('-created_at')

    featured = Projectmodel.objects.first()

    return render(request, 'civilengineering/projects.html', {
        'myprojects': projects,
        'comments': comments,
        'featured': featured,
        'query': query,
    })

# CATEGORY FILTER (IMPORTANT FOR YOUR UI)
def category_page(request, category):

    projects = Projectmodel.objects.filter(category=category)

    return render(
        request,
        'civilengineering/projects.html',
        {
            'myprojects': projects,
            'selected_category': category
        }
    )


# ADMIN LOGIN
def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('/admin')

        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'civilengineering/login.html')


# ADMIN SIGNUP (ONLY ONE SUPERUSER)
def signup_view(request):

    if User.objects.count() >= 1:
        return HttpResponse("No other account allowed!")

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        User.objects.create_superuser(
            username=username,
            password=password
        )

        return redirect('login_view')

    return render(request, 'civilengineering/signup.html')


# USER LOGIN (FIXED BUG)
def user_login(request):
    myuser = Usermodel.objects.all()

    if request.method == 'POST':

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('project')

        else:
            messages.error(request, "Invalid login details")

    return render(request, 'civilengineering/user_login.html', {"myuser":myuser})


# USER SIGNUP (FIXED)
def user_signup(request):

    if request.method == 'POST':

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confpassword = request.POST.get("confpassword")

        if password != confpassword:
            messages.error(request, 'Passwords do not match!')
            return redirect('user_signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists")
            return redirect('user_login')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, 'Account created successfully!')
        return redirect('user_login')

    return render(request, "civilengineering/user_signup.html")


# STATIC PAGES
def about(request):
    return render(request, 'civilengineering/about.html')

def contact(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"""
New Contact Message:

Name: {name}
Email: {email}

Message:
{message}
"""

        send_mail(
            subject=f"VitalFilms Contact from {name}",
            message=full_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=["vitalfilms@gmail.com"],
            fail_silently=False
        )

        messages.success(request, "Message sent successfully! Vital will respond as soon as possible🏃‍♂️")

        return redirect("contact")

    return render(request, "civilengineering/contact.html")


def privacy(request):
    return render(request, 'civilengineering/privacy.html')

def logout_view(request):
    logout(request)
    return redirect('home')



def watch_video(request, id):

    movie = get_object_or_404(
        Projectmodel,
        id=id
    )

    return render(
        request,
        'civilengineering/watch.html',
        {
            'movie': movie
        }
    )