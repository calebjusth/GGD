from django.forms import ModelForm
from django import forms
from .models import MembersList


class memberform(ModelForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    email = forms.TextInput()
    phone = forms.TextInput()
    choice = (
        ('Ethiopia', 'Ethiopia'),
        ('South Africa', 'South Africa'),
        ('Canada', 'Canada'),
    )
    address = forms.Textarea()    
    country = forms.ChoiceField(choices=choice, widget=forms.Select())
    


    class Meta:
        model = MembersList
        fields = [
            'first_name', 
            'last_name',
            'email',
            'phone',
            'address',
            'country',
            ]