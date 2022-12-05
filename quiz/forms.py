from django import forms
from . import models

class QuizForm(forms.ModelForm):
    class Meta:
        model = models.QuizModel
        fields = "__all__"