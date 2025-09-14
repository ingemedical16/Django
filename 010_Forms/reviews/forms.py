from django import forms

class ReviewFrom(forms.Form):
    user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
        "required": "Your name must not be empty",
        "max_length":"Plase enter a shorter name!"
    })
