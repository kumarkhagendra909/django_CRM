from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record


# Create your views here.
def home(request):
    records = Record.objects.all() 
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
        return render(request, 'home.html', {'records': records})



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

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "Need to login to view this page!")
        return redirect('home')

def new_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added....")
                return redirect('home')
        return render(request, 'new_record.html', {'form':form})
    else:
        messages.success(request, "Login first...")
        return redirect(request, 'home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated.....")
            return redirect('home')
        return render(request, 'update_record.html', {'form': form})
    else:
        messages.success(request, "Loggin first")
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        current_record.delete()
        messages.success(request, "Your Record Deleted Successfully.....")
        return redirect("home")
    else:
        messages.success(request, "Loggin first....")
        return redirect('home')
    
