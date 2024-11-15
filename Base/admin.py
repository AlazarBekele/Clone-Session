from django.contrib import admin
from .models import (
  JobDepartement,
  Apply
)

# Register your models here.

admin.site.register (JobDepartement)
admin.site.register (Apply)