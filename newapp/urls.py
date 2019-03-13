from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/<file_name>', views.read_file, name="rf"),
    path('home/', views.write_file, name='wf'),
    path('home/update/', views.update_file, name='uf'),
    path('home/delete/<file_name>', views.delete_file, name='df')
]