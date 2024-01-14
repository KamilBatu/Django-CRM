from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .forms import AddRecordForm
from .models import Record



# Create your views here.

def home(request):
    records=Record.objects.all()
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
    else:
        return render(request, 'home.html', {'records':records})
# def login_user(request):
#     pass
def logout_user(request):
    logout(request)
    messages.success(request, 'you have logged out successfuly')
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():  # Corrected the line here
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Successfully registered')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def record_customer(request, pk):

    if request.user.is_authenticated:
        record_customer=Record.objects.get(pk=pk)
        return render(request, 'record.html', {"record_customer":record_customer})
    else:
        messages.success(request, 'you have to login frist')
        return render(request, 'home.html')
def delete_record(request, pk):
    if request.user.is_authenticated:
        customer=Record.objects.get(pk=pk)
        customer.delete()
        messages.success(request, 'record deleted successfuly')
        return redirect('home')
    else:
        messages.error('you have to logged in to do that')
        return redirect('home')
    
def addRecord(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=='POST':
            if form.is_valid:
                form.save()
                messages.success(request, 'added successfuly')
                return redirect('home')
        else:
            return render(request, 'add_record.html', {'form':form})
    else:
        messages.error(request, 'you need to login frist')
        return redirect('home')
def update(request, pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(pk=pk)
        form=AddRecordForm(request.POST or None, instance=current_record)
        if request.method=='POST':
            if form.is_valid:
                form.save()
                messages.success(request, 'updated successfuly')
                return redirect('home')
        else:
            return render(request, 'update.html', {'form':form})
    else:
        messages.error(request, 'you need to login frist')
        return redirect('home')
