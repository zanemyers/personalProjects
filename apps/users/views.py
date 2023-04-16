from django.shortcuts import render
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
    return render(request, 'users/user-profile.html', context=context)