from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User

def register(request):
    if request.user.is_authenticated:
        return redirect('main:home')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone_number')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        
        
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('users:register')
        
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('users:register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('users:register')
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.phone_number = phone 
            user.save()

            messages.success(request, f"Account created for {username}!")
            return redirect('users:login')
            
        except Exception as e:
            messages.error(request, "Something went wrong during registration.")
            print(e)
            return redirect('users:register')

    return render(request, 'users/register.html')


def login_user(request):
    
    if request.user.is_authenticated:
        return redirect('main:home')

    if request.method == 'POST':
    
        username_val = request.POST.get('username')
        password_val = request.POST.get('password')

    
        user = authenticate(request, username=username_val, password=password_val)

        if user is not None:
    
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            
    
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('main:home')
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'users/login.html')