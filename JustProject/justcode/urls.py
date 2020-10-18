from django.contrib import admin
from django.urls import path, include

from justcode.views import show_vba, show_python

urlpatterns = [
    path('', show_vba, name='justcode vba'),
    path('vba', show_vba, name='justcode vba'),
    path('python/', show_python, name='justcode python'),
]
