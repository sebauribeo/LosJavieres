from django import forms
from .models import Product


class ProductForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'type': 'text',
            'placeholder': 'Ingresa el nombre del producto'
        }
    ))
    image = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'type': 'text',
            'placeholder': 'Ingresa la URL de la imagen'
        }
    ))
    price = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'type': 'number',
            'placeholder': 'Ingresa el precio del producto'
        }
    ))
    stock = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'type': 'text',
            'placeholder': 'Ingresa el stock'
        }
    ))
    details = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'type': 'text',
            'placeholder': 'Ingresa la descipción del producto'
        }
    ))
    brand = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'type': 'text',
            'placeholder': 'Ingresa la marca del producto'
        }
    ))
    category = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control mt-2',
            'type': 'text',
            'placeholder': 'Ingresa la categoria del producto'
        }
    ))

    class Meta:
        model = Product
        fields = ('name', 'image', 'price', 'stock', 'details', 'brand', 'category')


# class UserForm(forms.ModelForm):

#     name = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'class': 'form-control mt-2',
#             'type': 'text',
#             'placeholder': 'Ingresa tu nombre'
#         }
#     ))
#     lastName = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'class': 'form-control mt-2',
#             'type': 'text',
#             'placeholder': 'Ingresa tu apellido'
#         }
#     ))
#     email = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'class': 'form-control mt-2',
#             'type': 'email',
#             'placeholder': 'Ingresa el email'
#         }
#     ))
#     password = forms.CharField(widget=forms.TextInput(
#         attrs={
#             'class': 'form-control mt-2',
#             'type': 'password',
#             'placeholder': 'Ingresa la contraseña'
#         }
#     ))
#     class Meta:
#         model = User
#         fields = ('name', 'lastName', 'email', 'password')
