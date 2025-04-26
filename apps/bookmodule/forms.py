from django import forms
from . import models

class BookForm(forms.ModelForm):
    title = forms.CharField(
        max_length=50,
        required=True,
        label="Title",
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': "mycssclass",
            'id': 'jsID'
        })
    )

    price = forms.DecimalField(
        required=True,
        label="Price",
        initial=0
    )

    edition = forms.IntegerField(
        required=True,
        initial=0,
        widget=forms.NumberInput()
    )

    author = forms.CharField(
        max_length=50,
        required=True,
        label="Author",
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': "mycssclass",
            'id': 'jsID'
        })
    )

    class Meta:
        model = models.Book
        fields = ['title', 'price', 'edition', 'author']
