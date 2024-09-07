from django import forms
from apps.shop.models import Product, User


class StoreDetails(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'stock']


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password']


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']

        widgets={
       'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        'password': forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}),
        }


