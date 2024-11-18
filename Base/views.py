from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import InputForm
from django.contrib import messages
from .models import (
  JobDepartement,
  Apply
)
# Create your views here.

def index (request):

  form = InputForm(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, 'Sucssfully Added!!')
      form = InputForm()

  apply = Apply.objects.all()

  context = {
    'apply' : apply,
    'forms' : form
  }

  return render (request, 'index.html', context)




def login_check (request):
  
  form = InputForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():

      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')

      user = authenticate(request, username = username, password = password)

      if user is not None:
        login(request, user)
        return redirect ('index')
      
  context = {
    'from' : form
  }

  return render (request, 'Login_page.html', context=context)