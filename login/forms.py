from database import models
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import forms as UserForms



class DocumentForm(forms.Form):
    #username = forms.CharField(label="username")
    username = forms.CharField(label="username"
        ,widget=forms.TextInput(attrs={'class': 'form-control'}) )
    
    name = forms.CharField(label="name",widget=forms.TextInput(attrs={'class': 'form-control'}))
    speciality = forms.CharField(label="speciality",widget=forms.TextInput(attrs={'class': 'form-control'}))
    qualification = forms.CharField(label="qualification",widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(),label="password")   
    docfile = forms.FileField(
        label='Select an Image',
        help_text='max 1 megabytes'
    )

    '''def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget = TextInput(attrs={
            'id': 'myCustomId',
            'class': 'form-control',
            #'name': 'myCustomName',
            #'placeholder': 'myCustomPlaceholder'
            })
    '''

class Document2Form(forms.Form):
    #username = forms.CharField(label="username")
    username = forms.CharField(label="username"
         ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    name = forms.CharField(label="name"
         ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(),label="password")
    docfile = forms.FileField(
        label='Select an Image',
        help_text='max 1 megabytes'
    )


class Document3Form(forms.Form):
    #username = forms.CharField(label="username")
    username = forms.CharField(label="username"
         ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    name = forms.CharField(label="name"
         ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    age = forms.IntegerField(label="age"
         ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    weight=forms.IntegerField(label="weight"
         ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    height = forms.CharField(label="height"
         ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    reg_no=forms.CharField(label="reg_no" 
        ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(),label="password")
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