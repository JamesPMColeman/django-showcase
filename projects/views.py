from django.shortcuts import render
from projects.models import Project


def project_list(request):
	return render(request, 'projects/index.html')


def all_projects(request):
	# Get projects from db
	all_projects = Project.objects.all()
	print(all_projects)
	return render(request, 'projects/all_projects.html', {'projects': all_projects})
