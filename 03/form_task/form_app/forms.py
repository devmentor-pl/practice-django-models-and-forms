from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(label='email')
    message = forms.CharField(widget=forms.Textarea, min_length=20)
