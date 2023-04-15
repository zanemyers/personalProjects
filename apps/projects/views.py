from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all().order_by('created')
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context=context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {
        'project': project,
    }
    return render(request, 'projects/single_project.html', context=context)


def create_project(request):
    form = ProjectForm
    context = {
        'form': form,
    }

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    return render(request, 'projects/project_form.html', context=context)


def update_project(request, pk):
    project = Project.objects.get(pk=pk)
    form = ProjectForm(instance=project)
    context = {
        'form': form,
    }

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    return render(request, 'projects/project_form.html', context=context)


def delete_project(request, pk):
    project = Project.objects.get(pk=pk)

    if request.method == "POST":
        project.delete()
        return redirect('projects')

    return render(request, 'projects/delete.html', {'object': project})
