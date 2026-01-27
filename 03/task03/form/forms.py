from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(max_length=100)
    message = forms.CharField(min_length=20)
