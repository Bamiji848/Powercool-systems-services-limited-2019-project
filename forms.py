from django import forms
from .import models
from django.core import validators
from powercool_app.models import Contact,Comment,Quote

from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class QuoteForm(forms.ModelForm):
    SERVICES_CHOICES = [
        ('please select a service','Please Select a Service'),
        ('power conditioning and control System ',
         'Power Conditioning and Control System '),
        ('structured cabling for power and provision of clean earthen system',
         'Structured Cabling for Power and Provision of Clean Earthen System'),
        ('computer suite preparation (environment conditioning)',
         'Computer Suite Preparation (Environment Conditioning)'),
        ('automatic fire defense system based on FM 200 gas',
         'Automatic Fire Defense System based on FM 200 Gas.'),
        ('bts alarm/equipment status monitoring system ',
         'BTS Alarm/Equipment Status Monitoring System '),
        ('data center environmental monitoring system ',
         'Data Center Environmental Monitoring System '),
        ('dc power systems', 'DC Power Systems'),
        ('solar power', 'Solar Power'),
        ('consultancy and ad-hoc services', 'Consultancy and ad-hoc services'),
        ('precision cooling for data center and general cooling',
         'Precision cooling for Data Center and general cooling'),
    ]
    services = forms.CharField(label='Select prefered service',widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'select prefered service'}, choices=SERVICES_CHOICES))
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}))

    class Meta:
        model = Quote
        fields = ('services','name','email','message')
        widget = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }        
