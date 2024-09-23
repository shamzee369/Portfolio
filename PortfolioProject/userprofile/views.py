
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse
from .forms import LoginForm, UserProfileForm
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.decorators import login_required


# your_app/views.py

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import LoginForm, UserProfileForm  # Ensure both forms are imported
from .models import UserProfile  # Ensure UserProfile is imported

def register_view(request):
                if request.method == 'POST':
                    username = request.POST.get('username')
                    email = request.POST.get('email')
                    password1 = request.POST.get('password1')
                    password2 = request.POST.get('password2')
                    bio = request.POST.get('bio')
                    skills = request.POST.get('skills')
                    contact = request.POST.get('contact')
                    profile_image = request.FILES.get('profile_image')
            
                    if password1 != password2:
                        messages.error(request, "Passwords do not match")
                        return redirect('userprofile:firstpage')
            
                    if User.objects.filter(username=username).exists():
                        messages.error(request, "Username already exists")
                        return redirect('userprofile:firstpage')
            
                    try:
                        user = User.objects.create_user(username=username, email=email, password=password1)
                        user.save()
                    except Exception as e:
                        messages.error(request, f"Error creating user: {str(e)}")
                        return redirect('userprofile:firstpage')
            
                    # Add 'user_type' to POST data before passing it to the form
                    post_data = request.POST.copy()
                    post_data['user_type'] = 'user'
            
                    # Create the UserProfile form instance
                    form = UserProfileForm(post_data, request.FILES)
                    if form.is_valid():
                        user_profile = form.save(commit=False)
                        user_profile.user = user
                        user_profile.save()
            
                        messages.success(request, "Registration successful! Please log in.")
                        return redirect('userprofile:firstpage')
                    else:
                        print(f"UserProfileForm is not valid: {form.errors}")
                        messages.error(request, "There was an error in your profile information")
                        return redirect('userprofile:firstpage')
            
                else:
                    return redirect('userprofile:firstpage')              

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print("Form submission received")  # Debugging
        
        if form.is_valid():
            print("Form is valid")  # Debugging
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Use Django's built-in authenticate to check credentials
            user = authenticate(request, username=username, password=password)
            print(f"User authenticated: {user}")  # Debugging
    
            if user is not None:
                login(request, user)  # Log in the user using Django's built-in method
                print("User logged in successfully")  # Debugging
                
                # Fetch user profile
                try:
                    user_details = UserProfile.objects.get(user__username=username)
                    user_type = user_details.user_type
                    print(f"User type: {user_type}")  # Debugging
                    
                    if user_type == 'user':
                        return redirect('userprofile:profile')  # Redirect to profile page
                    elif user_type == 'admin':
                        return redirect('admin_dashboard')  # Update with your admin dashboard URL
                except UserProfile.DoesNotExist:
                    messages.error(request, 'User profile not found.')
                    return redirect('userprofile:firstpage')  # Redirect to firstpage
            else:
                messages.error(request, 'Invalid username or password.')
                print("Authentication failed")  # Debugging
                return redirect('userprofile:firstpage')  # Redirect to firstpage
        else:
            messages.error(request, 'Invalid form submission.')
            print("Form validation failed")  # Debugging
            return redirect('userprofile:firstpage')  # Redirect to firstpage
    else:
        # If GET request, redirect to firstpage
        return redirect('userprofile:firstpage')

@login_required
def profile_view(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)

    context = {
        'bio': user_profile.bio,
        'skills': user_profile.skills,
        'contact': user_profile.contact,
        'profile_image': user_profile.profile_image,  # Optional, if you want to display the profile image
    }

    return render(request, 'user/profile.html', context)


def logout_view(request):
    logout(request)  # Logs out the user
    messages.success(request, "You have successfully logged out.")
    return redirect('userprofile:login')


def firstpage_view(request):
    # Initialize empty forms or pre-populate if needed
    login_form = LoginForm()
    register_form = UserProfileForm()

 
    return render(request, 'firstpage.html', {
        'login_form': login_form,
        'register_form': register_form,
  
    })
