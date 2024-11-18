from django import forms
from .models import (
  JobDepartement,
  Apply,
)
class InputForm (forms.ModelForm):
  class Meta:

    model = Apply
    fields = '__all__'

    widgets = {
      'first_name' : forms.TextInput(attrs={
        'class' : 'form-control'
      }),
      'last_name' : forms.TextInput(attrs={
        'class' : 'form-control'
      }),
      'dob' : forms.DateInput(attrs={
        'class' : 'form-control',
        'type' : 'Date'
      }),
      'detail_about' : forms.Textarea(attrs={
        'class' : 'lead'
      })
    }

class login_Input(forms.Form):
  username = forms.CharField (widget=forms.TextInput(attrs={
    'class' : 'form-control',
    'placeholder' : 'Enter Email',
    'type' : 'email'
  })),
  password = forms.CharField (widget=forms.PasswordInput(attrs={
    'class' : 'form-control',
    'type' : 'password'
  }))