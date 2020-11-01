from django import forms

from app.forms.common import DisabledForm
from app.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        labels = {
            'time': 'Time (Minutes)',
            'image_url': 'Image URL',
        }
        fields = '__all__'


class DeleteRecipeForm(RecipeForm, DisabledForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledForm.__init__(self)