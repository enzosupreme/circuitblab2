from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    subject = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255)
    message = models.TextField(blank=True, null=True)

class Project(models.Model):
    category = models.ForeignKey(Category, related_name='projects', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    invisible = models.BooleanField(default=False)
    github = models.URLField(max_length=200, blank=True, null=True)
    youtube = models.URLField(max_length=200, blank=True, null=True)
    shop = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
