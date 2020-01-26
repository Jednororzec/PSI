from django import forms
from . import models

class SurveyCreationForm(forms.ModelForm):
    class Meta:
        model = models.Survey
        fields = ['name', 'description']
