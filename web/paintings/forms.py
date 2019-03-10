from django import forms


class CreatePaintingForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100)
    image = forms.CharField(label='Image', max_length=100)
    description = forms.CharField(label='Description', max_length=100)
    medium = forms.CharField(label='Medium', max_length=100)
    price = forms.CharField(label='Price', max_length=300)
    artist = forms.CharField(label='Artist', max_length=200)
