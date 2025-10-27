from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about_page, name='about'),
    path('contact/', views.contact, name='contact'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]


