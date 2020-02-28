from django import forms
from .models import Spending

class SpendingForm(forms.ModelForm):
    item = forms.CharField(max_length=64, help_text='Enter item name')
    price = forms.DecimalField(max_digits=14, decimal_places=4, help_text='Enter item price')

    class Meta:
        model = Spending
        fields = ['item', 'price']
    

