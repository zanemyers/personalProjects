from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import login, authenticate, logout
from .models import Profile


def profiles(request):
    profiles = Profile.objects.all().order_by('created')
    context = {
        'profiles': profiles,
    }
    return render(request, 'users/profiles.html', context=context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description__exact='')
    other_skills = profile.skill_set.filter(description__exact='')
    context = {
        'profile': profile,
        'top_skills': top_skills,
        'other_skills': other_skills,
    }
    return render(request, 'users/user_ profile.html', context=context)


def loginUser(request):
    page = 'login'
    context = {
        'page': page,
    }
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, 'Username does not exist.')
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('profiles')
        else:
            messages.error(request, 'Username or Password is incorrect.')

    return render(request, 'users/login_register.html', context=context)


def logoutUser(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    context = {
        'page': page,
        'form': form,
    }

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'Account was created for ' + user.username)
            login(request, user)

            return redirect('profiles')
        else:
            context['form'] = form
            messages.error(request, 'An error has occurred during registration.')

    return render(request, 'users/login_register.html', context=context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects,
    }
    return render(request, 'users/account.html', context=context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm()
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'users/profile_form.html', context=context)
