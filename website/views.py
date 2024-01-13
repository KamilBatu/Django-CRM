from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you have been logged in successfuly')
            return redirect('home')
        else:
            messages.error(request, 'something wrong please try again')
            return redirect('home')
    return render(request, 'home.html')
# def login_user(request):
#     pass
def logout_user(request):
    logout(request)
    messages.success(request, 'you have logged out successfuly')
    return redirect('home')
def register(request):
    return render(request, 'register.html')