from django import forms
from .models import (
  JobDepartement,
  Apply
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
      })
    }