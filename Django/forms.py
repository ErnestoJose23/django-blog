from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    contect = forms.CharField(widget=forms.Textarea)