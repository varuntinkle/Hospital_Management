from database import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import forms as UserForms



class DocumentForm(forms.Form):
	#username = forms.CharField(label="username")
    username = forms.CharField(label="username")
    password = forms.CharField(label="password")
    name = forms.CharField(label="name")
    speciality = forms.CharField(label="speciality")
    qualification = forms.CharField(label="qualification")
    docfile = forms.FileField(
        label='Select an Image',
        help_text='max 1 megabytes'
    )


class Document2Form(forms.Form):
    #username = forms.CharField(label="username")
    username = forms.CharField(label="username")
    password = forms.CharField(label="password")
    name = forms.CharField(label="name")
    docfile = forms.FileField(
        label='Select an Image',
        help_text='max 1 megabytes'
    )



'''class DoctorForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password")
    name = forms.CharField(label="name")
    speciality = forms.CharField(label="speciality")
    qualification = forms.CharField(label="qualification")
    image = forms.FileField(label="Choose image")
'''