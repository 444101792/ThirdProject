from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 5, 
                'placeholder': 'Type your message here...'
            })
        }

class AdminReplyForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['admin_reply']
        widgets = {
            'admin_reply': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Type your reply here...'
            })
        }