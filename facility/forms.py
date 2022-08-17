from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='location_input', max_length=100)