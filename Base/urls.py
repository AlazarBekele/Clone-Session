from django.urls import path
from .views import (
    index,
    login_check,
    detail_page
)


urlpatterns = [
    path ('', index, name='index'),
    path ('login/', login_check, name='login'),
    path ('detail/<int:id>/', detail_page, name='detail_page')
]
