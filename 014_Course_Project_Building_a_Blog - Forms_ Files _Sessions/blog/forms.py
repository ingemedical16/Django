from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user_name', 'user_email', 'text']
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Comment', 'rows': 4}),
        }
        labels = {
            'user_name': 'Your Name',
            'user_email': 'Your Email',
            'text': 'Your Comment',
        }
        help_texts = {
            'text': 'Please enter at least 4 characters.',
        }
        error_messages = {
            'text': {
                'min_length': 'Comment is too short. Minimum 4 characters required.',
            },
        }   

