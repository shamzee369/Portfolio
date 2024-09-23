# views.py
from django.shortcuts import render, redirect,get_object_or_404
from .forms import EducationForm, CertificationForm, WorkExperienceForm, ProjectForm
from django.contrib.auth.decorators import login_required
from.models import Project
from userprofile.models import UserProfile
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from collections import defaultdict
from.models  import Project,UserProfile

@login_required
def addproject(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            project.user = user_profile
            project.save()
            return redirect('portfolio:portfolio')
    else:
        form = ProjectForm()
    return render(request, 'user/addproject.html', {'form': form})

@login_required
def addeducation(request):
    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            education = form.save(commit=False)
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            education.user_profile = user_profile  # Correct assignment
            education.save()
            return redirect('portfolio:portfolio')
    else:
        form = EducationForm()
    return render(request, 'user/education.html', {'form': form})

@login_required
def addwrkexp(request):
    if request.method == 'POST':
        form = WorkExperienceForm(request.POST)
        if form.is_valid():
            wrkexp = form.save(commit=False)
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            wrkexp.user_profile = user_profile  # Correct assignment
            wrkexp.save()
            return redirect('portfolio:wrkexp')
    else:
        form = WorkExperienceForm()
    return render(request, 'user/wrkexp.html', {'form': form})

@login_required
def addcertifi(request):
    if request.method == 'POST':
        form = CertificationForm(request.POST)
        if form.is_valid():
            cert = form.save(commit=False)
            user_profile, created = UserProfile.objects.get_or_create(user=request.user)
            cert.user_profile = user_profile  # Correct assignment
            cert.save()
            return redirect('portfolio:portfolio')
    else:
        form = CertificationForm()
    return render(request, 'user/certification.html', {'form': form})

from django.core.paginator import Paginator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def project_showcase(request):
    user = request.user
    # Retrieve or create the UserProfile for the current user
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    
    # Query the Project model using the UserProfile instance
    all_projects = Project.objects.filter(user=user_profile).order_by('-created_at')
    
    # Featured Projects (assuming they should appear on every page)
    featured_projects = all_projects.filter(is_featured=True)
    
    # Exclude featured projects from the paginated all_projects
    paginated_projects = all_projects.exclude(id__in=featured_projects.values_list('id', flat=True))
    
    paginator = Paginator(paginated_projects, 3)  # Show 4 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'featured_projects': featured_projects,
        'profile_user': user,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    
    return render(request, 'user/project_showcase.html', context)

# def user_project_showcase(request, username):
#     """
#     Displays all projects for a given user identified by username.
#     """
#     # Retrieve the User instance based on the provided username
#     profile_user = get_object_or_404(User, username=username)
    
    
#     # Retrieve the UserProfile associated with the User
#     user_profile = get_object_or_404(UserProfile, user=profile_user)
    
#     # Fetch all projects associated with this UserProfile
#     projects = Project.objects.filter(user=user_profile).order_by('-created_at')

    # paginator = Paginator(projects, 4)  # Show 10 projects per page
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    
#     # Optionally, fetch featured projects if applicable
#     featured_projects = projects.filter(is_featured=True)  # Ensure 'is_featured' exists
    
#     context = {
#         'projects': projects,
#         'featured_projects': featured_projects,
#         'profile_user': profile_user, # Pass the user to the template for context
#         'page_obj': page_obj,
#         'is_paginated': page_obj.has_other_pages(),
#         }
    
#     return render(request, 'user/project_showcase.html', context)


# def all_users_projects_showcase(request):
#     # Retrieve all users and their respective projects
#     all_users = User.objects.all()
    
#     # Create a dictionary to hold each user's profile and their projects
#     user_projects = defaultdict(list)
    
#     for user in all_users:
#         try:
#             # Try to get the UserProfile for the current user
#             user_profile = UserProfile.objects.get(user=user)
            
#             # Fetch the user's projects
#             projects = Project.objects.filter(user=user_profile).order_by('-created_at')
            
#             # Debug: Output project count for each user
#             print(f"User: {user.username}, Projects found: {projects.count()}")
            
#             if projects.exists():
#                 user_projects[user_profile] = projects
            
#         except UserProfile.DoesNotExist:
#             # Skip the user if no UserProfile is found
#             print(f"UserProfile not found for user: {user.username}")
#             continue
    
#     context = {
#         'user_projects': user_projects,
#     }
    
#     return render(request, 'user/all_projects_showcase.html', context)
def all_users_projects_showcase(request):
    # Retrieve all users and their respective projects
    all_users = User.objects.all()
    
    # Create a dictionary to hold each user's profile and their projects
    user_projects = defaultdict(list)
    
    for user in all_users:
        try:
            # Try to get the UserProfile for the current user
            user_profile = UserProfile.objects.get(user=user)
            
            # Fetch the user's projects
            projects = Project.objects.filter(user=user_profile).order_by('-created_at')
            
            # Debug: Output project count for each user
            print(f"User: {user.username}, Projects found: {projects.count()}")
            
            if projects.exists():
                user_projects[user_profile] = projects
            
        except UserProfile.DoesNotExist:
            # Skip the user if no UserProfile is found
            print(f"UserProfile not found for user: {user.username}")
            continue
    
    # Convert defaultdict to a regular dict
    user_projects_dict = dict(user_projects)
    
    context = {
        'user_projects': user_projects_dict,
    }
    
    return render(request, 'user/all_projects_showcase.html', context)