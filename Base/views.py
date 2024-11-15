from django.shortcuts import render
from .models import (
  JobDepartement,
  Apply
)
# Create your views here.

def index (request):

  apply = Apply.objects.all()

  context = {
    'apply' : apply
  }

  return render (request, 'index.html', context=context)