from django.shortcuts import render
from .models import (
  JobDepartement,
  Apply
)
from .forms import InputForm
# Create your views here.

def index (request):

  apply = Apply.objects.all()

  forms = InputForm(request.POST)

  context = {
    'apply' : apply,
    'forms' : forms
  }

  return render (request, 'index.html', context=context)