from django import forms
from .models import Brand, ProductType, Seller

class EarphoneFilterForm(forms.Form):
    min_price = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_price = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    product_type = forms.ModelChoiceField(queryset=ProductType.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    seller = forms.ModelChoiceField(queryset=Seller.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control'}))
    product_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    min_warranty = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    max_warranty = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
