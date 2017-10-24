from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.forms import SignUpForm, UserEditForm, ProfileEditForm
from django.contrib import messages
from accounts.models import Profile
from django.contrib.auth import authenticate


def index(request):
    return render(request, 'index.html', {})


def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect('accounts:index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


# social login
# @login_required
# def home(request):
#   return render(request, 'registration/login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def contact(request):
    return render(request, 'contact.html', {})

