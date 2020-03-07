from django import forms
from .models import Spending, Goal

class SpendingForm(forms.ModelForm):
    item = forms.CharField(max_length=64, help_text='Enter item name')
    price = forms.DecimalField(max_digits=14, decimal_places=4, help_text='Enter item price (format as 0 or 0.00)')

    class Meta:
        model = Spending
        fields = ['item', 'price']

class NewGoal(forms.ModelForm):
    ntsDuration = forms.CharField(max_length=64, help_text='Enter goal duration', label='Goal Duration')
    percentGoal = forms.DecimalField(max_digits=4, decimal_places=2, help_text='Enter percent goal (format as 0 or 0.00)', label='Percent Goal (%)')
    checkAmount = forms.DecimalField(max_digits=14, decimal_places=2, help_text='Enter check amount (format as 0 or 0.00)', label='Check Amount ($)')
    class Meta:
        model = Goal
        fields = ['checkAmount', 'percentGoal', 'ntsDuration']
    

