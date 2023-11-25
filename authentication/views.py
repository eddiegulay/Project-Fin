from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, privilege

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a profile for the user
            Profile.objects.create(user=user)
            # Log in the user after registration
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
        else:
            # Handle invalid login
            return render(request, 'registration/login.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'registration/login.html')


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        account_type = request.POST.get('account_type')

        # get the privilege object
        privilege_obj = privilege.objects.get(privilege_name=account_type)

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)

        # Additional processing for account type, if needed
        Profile.objects.create(user=user, privilege=privilege_obj)

        login(request, user)
        return redirect('home')  # Replace 'home' with the URL name of your home page

    return render(request, 'registration/register.html')
