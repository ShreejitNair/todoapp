from django import forms

class TodolistForm(forms.Form):
    text = forms.CharField(max_length=45,
        widget=forms.TextInput(
            attrs={'class': 'form control' ,'placeholder':'Enter todo e.g Grocery Shopping', 'aria-describeby': 'add-btn'}))
            