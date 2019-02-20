from django.db import models
from django.forms import ModelForm
from .models import Painting


class PaintingForm(ModelForm):
    class Meta:
        model = Painting
        fields = ['title', 'image', 'description', 'medium', 'price', 'artist', 'seller']
