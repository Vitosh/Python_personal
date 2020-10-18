from django.contrib import admin
from django.urls import path

from vitoshacademy.views import show_info, show_about

urlpatterns = [
    path('', show_info, name='vitoshacademy index'),
    path('about/', show_about, name='vitoshacademy about'),
]
