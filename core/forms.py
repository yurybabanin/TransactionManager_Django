from django import forms
from .models import Transactions

class PostFrom(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = ('name', 'note', 'sum')
