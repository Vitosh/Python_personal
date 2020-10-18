from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vitoshacademy/', include('vitoshacademy.urls')),
    path('justcode/', include('justcode.urls')),
]
