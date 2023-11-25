from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Privilege


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')  # Replace 'home' with the URL name of your home page
        else:
            # Handle invalid login
            return render(request, 'auth/sign-in.html', {'error_message': 'Invalid login credentials'})
    else:
        return render(request, 'auth/sign-in.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        account_type = request.POST.get('account-type')

        # get the privilege object
        privilege_obj = Privilege.objects.get(privilege_name=account_type)

        user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)

        # Additional processing for account type, if needed
        Profile.objects.create(user=user, privilege=privilege_obj)

        login(request, user)
        return redirect('home')

    else:
        # get the privilege object
        privilege_obj = Privilege.objects.all()

    return render(request, 'auth/sign-up.html', {'privilege': privilege_obj})


def user_logout(request):
    logout(request)
    return redirect('login')