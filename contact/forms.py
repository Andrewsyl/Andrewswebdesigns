from django.forms import ModelForm
from contact.models import ContactForm
from django import forms

class ContactView(ModelForm):
    message = forms.CharField(widget=forms.Textarea)

    class Meta:  # fields that will be on webpage
        model = ContactForm
        fields = ('name', 'email', 'topic', 'message')
