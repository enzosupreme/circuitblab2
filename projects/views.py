from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q

from .forms import NewProjectForm, EditProjectForm
from .models import Project, Category

def detail(request, pk):
    projects = get_object_or_404(Project, pk=pk)
    related_projects = Project.objects.filter(category=projects.category).exclude(pk=pk)[0:3]


    return render(request, 'projects/detail.html', {
        'projects': projects,
        'related_projects': related_projects
    })

def Categories(request,pk):
    projects = get_object_or_404(Project, pk=pk)
    category = Project.objects.filter(category=projects.category)
    query = request.Get.get('query', category.name)

    return render(request, 'projects/projects.html', {
        'projects': projects,
        'category': category,
        'query' : query,
    })


def projects(request):
    query = request.Get.get('query', projects.category)
    category_id = request.GET('category', 0)
    projects = Project.object.filter(invisible=False)
    categories = Category.objects.all()

    if category_id:
        projects = projects.filter(category_id=category_id)
    if query:
        projects = projects.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request, 'projects/projects.html', {
        'projects': projects,
        'query':query,
        'category':category,
        'category_id': int(category_id)
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)

        if form.is_valid():
            projects = form.save(commit=False)
            projects.created_by = request.user
            projects.save()

            return redirect('projects:detail', pk=projects.id)

    else:
        form = NewProjectForm()

    return render(request, 'projects/form.html', {
        'form': form,
        'title': 'New Project'
    })

@login_required
def edit(request, pk):
    projects = get_object_or_404(Project, pk=pk)

    if request.method == 'POST':
        form = EditProjectForm(request.POST, request.FILES, instance=projects)

        if form.is_valid():
            projects = form.save(commit=False)
            projects.created_by = request.user
            projects.save()

            return redirect('projects:detail', pk=projects.id)

    else:
        form = EditProjectForm(instance=projects)

    return render(request, 'projects/form.html', {
        'form': form,
        'title': 'Edit Project'
    })

