from django.urls import path
from .views import (
    index,
    login_check
)


urlpatterns = [
    path ('', index, name='index'),
    path ('login/', login_check, name='login')
]
