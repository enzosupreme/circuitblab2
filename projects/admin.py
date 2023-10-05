from django.contrib import admin

from .models import Category, Project, Service,ServiceRequest


admin.site.register(Category)
admin.site.register(Project)
admin.site.register(Service)
admin.site.register(ServiceRequest)
