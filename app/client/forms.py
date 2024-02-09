from django import forms
from .models import Client, DocumentAttachment

class LegalRequestForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'email', 'phone']
    
    case_description = forms.CharField(widget=forms.Textarea)
    case_type = forms.CharField(max_length=100)

class DocumentAttachmentForm(forms.ModelForm):
    class Meta:
        model = DocumentAttachment
        fields = ['document']
