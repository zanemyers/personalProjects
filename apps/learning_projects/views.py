from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LearningProject
from .forms import LearningProjectForm


def learning_projects(request):
    projects = LearningProject.objects.all().order_by('created')
    context = {'projects': projects}
    return render(request, 'learning_projects/learning_projects.html', context=context)


def learning_project(request, pk):
    project = LearningProject.objects.get(id=pk)
    context = {
        'project': project,
    }
    return render(request, 'learning_projects/learning_projects.html', context=context)


def create_project(request):
    form = LearningProjectForm
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = LearningProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    return render(request, 'learning_projects/project_form.html', context=context)


def update_project(request, pk):
    project = LearningProject.objects.get(pk=pk)
    form = LearningProjectForm(instance=project)
    context = {
        'form': form,
    }

    if request.method == "POST":
        form = LearningProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    return render(request, 'learning_projects/project_form.html', context=context)


def delete_project(request, pk):
    project = LearningProject.objects.get(pk=pk)

    if request.method == "POST":
        project.delete()
        return redirect('projects')

    return render(request, 'learning_projects/delete.html', {'object': project})
