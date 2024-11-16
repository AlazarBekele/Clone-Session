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

@login_required
def index (request):

  apply = Apply.objects.all()

  form = InputForm(request.POST or None)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success(request, 'Sucssfully Added!!')

      form = InputForm()

  context = {
    'apply' : apply,
    'form' : form
  }

  return render (request, 'index.html', context=context)


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