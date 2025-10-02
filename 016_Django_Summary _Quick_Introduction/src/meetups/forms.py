from django  import forms


class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your Email')
    name = forms.CharField(max_length=200, label='Your Full Name')
