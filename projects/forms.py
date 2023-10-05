from django import forms

from .models import Project

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('category', 'name','description', 'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }




class EditProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('category', 'name','description', 'image',)

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
        }