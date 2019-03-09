from django import forms


class SellerRegisterForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    phone = forms.CharField(label='Phone', max_length=100)
    description = forms.CharField(label='Description', max_length=300)
    logo = forms.CharField(label='Logo Link', max_length=200)
