from django import forms
from . import models
from .models import Address,Address2

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



class StudentForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        required=True,
        label="Name",
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': "mycssclass",
            'id': 'jsID'
        })
    )

    age = forms.IntegerField(
        required=True,
        label="Age",
        initial=7
    )
    ### Address = forms.ModelChoiceField(
    ###   queryset=Address.objects.all(),
    ###    empty_label=None,
    ###    required=True,
    ###    label="Adress",
    ###    widget=forms.Select(attrs={
    ###        'class': 'mycssclass',
    ###        'id': 'jsID2'
    ###    }))

    class Meta:
        model = models.Student
        fields = ['name','age','address']
        
        
class Student2Form(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        required=True,
        label="Name",
        widget=forms.TextInput(attrs={
            'placeholder': '',
            'class': "mycssclass",
            'id': 'jsID'
        })
    )

    age = forms.IntegerField(
        required=True,
        label="Age",
        initial=7
    )
    address = forms.ModelMultipleChoiceField(
        label="address",
        queryset=Address2.objects.all().order_by("student2"),
        widget=forms.CheckboxSelectMultiple()
    )


    class Meta:
        model = models.Student2
        fields = ['name','age','address']
        
        
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ['title', 'image']
