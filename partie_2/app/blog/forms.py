from tkinter import Widget
from django import forms

class CommentForm(forms.Form):
    author=forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Nom'
        })
    )
    body=forms.CharField(
        widget=forms.Textarea(attrs={
            'class':'form-control',
            'placeholder':'Votre commentaire'
        })
    )
    