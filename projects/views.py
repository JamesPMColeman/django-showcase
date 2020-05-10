from django.shortcuts import render
from projects.models import Project


def project_list(request):
	return render(request, 'projects/index.html')


def all_projects(request):
	# Get projects from db
	all_projects = Project.objects.all()
	print(all_projects)
	return render(request, 'projects/all_projects.html',
				  {'projects': all_projects})

def project_page(request, primary_key):
	project = Project.objects.get(pk=primary_key)
	return render(request, 'projects/read_more.html',
				  {'project': project})