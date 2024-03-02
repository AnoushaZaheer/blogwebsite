from django import forms
from .models import comments
from blog.models import Contact

class commentform(forms.ModelForm):
    class Meta:
        model=comments
        fields= ('name','email','body')


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
