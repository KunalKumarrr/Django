from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FeedbackForm
from .models import Feedback
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.contrib.auth.models import User

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Validate that passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register_user')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('register_user')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('register_user')

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Automatically log the user in after successful registration
        login(request, user)
        messages.success(request, "Registration successful! You are now logged in.")
        return redirect('feedback_form')  # Redirect to feedback form after login

    return render(request, 'register.html')

def home(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'home.html', {'feedbacks': feedbacks})

# Session-based authentication logic

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # If authentication is successful, log the user in
            login(request, user)  # This automatically manages the session
            return redirect('feedback_form')  # Redirect to the feedback form or home page
        else:
            # If authentication fails, show an error message
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')

@login_required
def feedback_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        rating = request.POST['rating']
        comments = request.POST['comments']

        # Save feedback to the database
        feedback = Feedback(name=name, email=email, rating=rating, comments=comments)
        feedback.save()

        messages.success(request, "Thank you for your feedback!")
        return redirect('home')

    return render(request, 'feedback_form.html')
def feedback_thanks(request):
    return render(request, 'thanks.html')

def logout_user(request):
    logout(request)  # This clears the session
    return redirect('login_user')
