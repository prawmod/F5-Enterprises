from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.db.models.fields import return_None
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import request


# Create your views here.

def homepage(request):
    return HttpResponse("<h1>Welcome to my homepage!</h1>")


#Register View

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form=UserCreationForm()
    return render(request, 'inventory/register.html',{'form': form})

#login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'inventory/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('homepage')
