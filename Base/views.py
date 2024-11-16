from django.shortcuts import render
from django.contrib.auth.decorators import login_Input
from .forms import InputForm, loginForm
from .models import (
  JobDepartement,
  Apply
)
# Create your views here.

@login_Input(login_url='')
def index (request):

  apply = Apply.objects.all()

  forms = InputForm(request.POST)

  context = {
    'apply' : apply,
    'forms' : forms
  }

  return render (request, 'index.html', context=context)

def login_check (request):

  froms = loginForm