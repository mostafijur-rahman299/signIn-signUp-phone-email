from django.shortcuts import render,redirect

from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login, authenticate

def user_register(request):
    if request.method == 'POST':
        register_form = RegistrationForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            return redirect('/')
    else:
        register_form = RegistrationForm()
    context = {
        'form': register_form
    }
    return render(request, 'registration.html', context)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user:
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('/')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def home(request):
    return render(request, 'home.html')

