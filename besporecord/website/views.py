from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
def home(request):
    # check to see if logging in 
    if request.method == 'POST':
        # do something
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate and login
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "You Faled to loggin")
    else:
        return render(request, 'home.html', {})



def register_user(request):
    # todo registering new user to our website
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Thank you for registering to our CRM, You have been successfully registered")
            return redirect('home')
    else: 
        form = SignUpForm()       
        return render(request, 'register.html', {'form': form})
        
    return render(request, 'register.html', {'form': form})

def login_user(request):
    pass

def logout_user(request):
    # todo for logout the user
    logout(request)
    messages.success(request, "You have been logout")
    return redirect('home')