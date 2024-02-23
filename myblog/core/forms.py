from django import forms
from .models import comments

class commentform(forms.ModelForm):
    class Meta:
        model=comments
        fields= ('name','email','body')
