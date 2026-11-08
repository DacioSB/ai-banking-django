from django import forms

from banking.models import BankingDocument


class DocumentUploadForm(forms.ModelForm):
    
    class Meta:
        model = BankingDocument()
        fields = ['title', 'content', 'document_type', 'customer_name', 'customer_id', 'status']
        widgets = {
            "content": forms.Textarea(attrs={"rows": 8, "placeholder": "Paste or type the full document content here..."}),
            "title": forms.Textarea(attrs={"placeholder": "e.g. Loan Application – John Smith"}),
            "customer_name": forms.Textarea(attrs={"placeholder": "e.g. John Smith"}),
            "customer_id": forms.Textarea(attrs={"placeholder": "e.g. CUST-001"}),
        }
    