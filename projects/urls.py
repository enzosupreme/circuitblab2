from django.urls import path, include

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('browse/', include('browse.urls')),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
]