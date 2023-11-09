from django.forms import ModelForm
from .models import *
from django import forms

class partnerform(ModelForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.EmailInput()
    phone = forms.TextInput()
    choice = (
        ('10$', '10$'),
        ('50$', '50$'),
        ('100$', '100$'),
        ('500$', '500$'),
        ('1000$', '1000$'),
        ('2000$', '2000$'),
        ('5000$', '5000$'),
    )
    amount = forms.ChoiceField(choices=choice, widget=forms.Select())
    choice2 = (
        ('once', 'once'),
        ('weekly', 'weekly'),
        ('monthly', 'monthly'),
    )
    pledge = forms.ChoiceField(choices=choice2, widget=forms.Select())
    address = forms.Textarea()

    class Meta:
        model = Partner
        fields = [
            'first_name', 
            'last_name',
            'email',
            'phone',
            'amount',
            'pledge',
            'address',
            ]