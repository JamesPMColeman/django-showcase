from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('', views.all_projects, name='all_projects'),
    path('<int:primary_key>', views.project_page, name='read_more')
]
