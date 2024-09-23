# forms.py
from django import forms
from .models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image','is_featured']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter project title',
                'required': 'required'
            }),
            
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter project description',
                'rows': 4,
                'required': 'required'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'is_featured': forms.CheckboxInput(attrs={
                'class': 'form-check-input'})
            
        }

# forms.py
from django import forms
from .models import WorkExperience

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['title', 'company', 'start_date', 'end_date', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job title',
                'required': 'required'
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter company name',
                'required': 'required'
            }),
            'start_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': 'required'
            }),
            'end_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter job description',
                'rows': 4,
                'required': 'required'
            }),
        }


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'graduation_date']
        widgets = {
            'institution': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter institution name',
                'required': 'required'
            }),
            'degree': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter degree obtained',
                'required': 'required'
            }),
            'graduation_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': 'required'
            }),
        }


class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name', 'date_obtained']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter certification name',
                'required': 'required'
            }),
            'date_obtained': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': 'required'
            }),
        }
