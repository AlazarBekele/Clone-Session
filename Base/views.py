from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import InputForm, login_Input
from django.http import HttpResponse
from django.contrib import messages
from .models import (
  JobDepartement,
  Apply
)
# Create your views here.
@login_required (login_url='/login/')
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

@login_required (login_url='/login/')
def detail_page (request, id):

  try:
    apply = Apply.objects.get(pk=id)
  except:
    return HttpResponse ('Bad Request!!')
  
  form = InputForm(request.POST or None, instance=apply)

  if request.method == 'POST':
    if form.is_valid():
      form.save()
      messages.success (request, 'Succssfully Updateed!!')

      return redirect ('index')
    
  context = {
      'form' :form,
      'apply' : apply
  }

  return render (request, 'Base/detail_page.html', context=context)


def detail_delete (request, det_id):
  try:
    apply = Apply.objects.get(pk=det_id)
  except:
    return HttpResponse ('Bad Request!!')
  
  apply.delete()
  messages.success(request, 'Successfully Deleted!!')
  return redirect ('index')


def login_check (request):
  
  form = login_Input(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():

      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      

      user = authenticate(request, username=username, password=password)
      
      if user is None:
        messages.success (request, 'Compleate Your Task!!')

      elif user is not None:
        login(request, user)
        messages.success (request, 'The user is Correct!!')
        return redirect ('index')        
      
  context = {
    'form' : form,
  }

  return render (request, 'Base/Login_page.html', context)