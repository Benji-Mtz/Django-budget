# Importing required libraries
from django import forms


class ExpenseForm(forms.Form):

    title = forms.CharField()
    amount = forms.IntegerField()
    category = forms.CharField()

    widget = {
        'title': forms.TextInput(attrs={'class': 'input-group form-control form-control-lg'}),
        'amount': forms.TextInput(attrs={'class': 'input-group form-control form-control-lg'}),
    }
