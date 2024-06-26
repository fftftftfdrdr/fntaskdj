from django import forms
from .models import Client, Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'photo']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['client', 'products', 'total_amount']
    
    client = forms.ModelChoiceField(queryset=Client.objects.all(), required=True)
    products = forms.ModelMultipleChoiceField(queryset=Product.objects.all(), widget=forms.CheckboxSelectMultiple, required=True)
    total_amount = forms.DecimalField(max_digits=10, decimal_places=2, required=True)

