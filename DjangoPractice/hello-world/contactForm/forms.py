from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from contactForm.models import Contact

class ContactForm (ModelForm):
    class Meta():
        model = Contact
        fields=[
            'first_name',
            'last_name',
            'email',
            'phone',
            'description'
        ]
