from django.conf.urls import include
from django.urls import re_path
from . import views

urlpatterns = [
    re_path('^callback/', views.callback),
]