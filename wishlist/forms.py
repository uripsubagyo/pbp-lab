
from django import forms

class BarangWishlistAdd(forms.Form):
    nama = forms.CharField(widget=forms.TextInput(attrs={'name':'nama'}))
    harga = forms.CharField(widget=forms.TextInput(attrs={'name':'harga'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'name':'description'}))
    
