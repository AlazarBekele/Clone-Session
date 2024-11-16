from django.shortcuts import render
from django.contrib.auth.decorators import login_Input
from .forms import InputForm
from django.contrib import messages
from .models import (
  JobDepartement,
  Apply
)
# Create your views here.

@login_Input(login_url='')
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