from django.urls import path

from app.views.index import index
from app.views.recipes import recipe_create, recipe_edit, recipe_delete, recipe_details

urlpatterns = (
    path('', index, name='index'),
    path('create/', recipe_create, name='recipe create'),
    path('edit/<int:pk>', recipe_edit, name='recipe edit'),
    path('delete/<int:pk>', recipe_delete, name='recipe delete'),
    path('details/<int:pk>', recipe_details, name='recipe details'),
)