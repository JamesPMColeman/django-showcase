from django.shortcuts import render
from django.http import HttpResponse


def project_list(request):
	return HttpResponse("<h1>First Django Web Page</h1>")
