from django.contrib.admin import forms

from banking.models import BankingDocument


class Form(forms.ModelForm):
    
    class Meta:
        model = BankingDocument()
        fields = ['title', 'content', 'document_type', 'customer_name', 'customer_id', 'status']
        widgets = {
            "content": forms.TextArea(attrs={"rows": 8, "placeholder": "Paste or type the full document content here..."}),
            "title": forms.TextArea(attrs={"placeholder": "e.g. Loan Application – John Smith"}),
            "customer_name": forms.TextArea(attrs={"placeholder": "e.g. John Smith"}),
            "customer_id": forms.TextArea(attrs={"placeholder": "e.g. CUST-001"}),
        }
    