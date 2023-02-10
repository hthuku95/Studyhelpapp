from django import forms
from django.forms import MultipleChoiceField, ChoiceField
import random

class ContactForm(forms.Form):
    name = forms.CharField(label='', max_length=100,widget=forms.TextInput(attrs={'name':'name','id':'name'}))
    email = forms.EmailField( label='',max_length=100 ,widget=forms.EmailInput(attrs={'name':'email','id':'email'}))
    message = forms.CharField( label='',widget=forms.Textarea(attrs={'id':'message','name':'message','rows':5}))




