from django.urls import path
from .views import (
    index,
    login_check,
    detail_page,
    detail_delete
)


urlpatterns = [
    path ('', index, name='index'),
    path ('login/', login_check, name='login'),
    path ('detail/<str:id>/', detail_page, name='detail_page'),
    path ('detaildelete/<str:det_id>/', detail_delete, name='detail_delete')
]
