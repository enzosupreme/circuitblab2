from django import forms

from projects.models import Category, Project, Service, ServiceRequest


INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class ServiceForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ('subject','email', 'message')

        widgets = {
            'subject': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'email': forms.EmailInput(attrs={
                'class': INPUT_CLASSES
            }),
            'message': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),

        }