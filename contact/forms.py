from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': 'editContent', 'placeholder': 'Your email...'}))

    class Meta:
        model = Contact
        fields = ('email', )