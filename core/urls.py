from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('services/', views.services, name='services'),
    path('browse/', include('browse.urls')),
    path('commission/', views.commission, name='commission'),
]