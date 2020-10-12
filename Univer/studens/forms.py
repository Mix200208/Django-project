from django import forms
from django.forms import ModelForm
from .models import Rate


class RateLesson(ModelForm):
    class Meta:
        model = Rate
        fields = ("rate",)


