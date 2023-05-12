from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from django.contrib import messages

# Create your views here.


def registerpage(request):
    if request.method=="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse('Your registration is successful')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'practice/register.html', context)


def homepage(request):
    return render(request, 'practice/home.html')

def loginpage(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials supplied")
            return redirect("login")
    return render(request, 'practice/login.html')



