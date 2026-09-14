from django.contrib import admin

from banking.models import BankingDocument, WorkflowTask

# Register your models here.
# @admin.register(BankingDocument)
# @admin.register(WorkflowTask)
# the class extends from admin.ModelAdmin
#in the list display is an array: 'title', 'document_type', 'status', 'customer_name', 'customer_id', 'created_at'
# in filter: document type and status
#you can search by title, customer_name and customer_id
#readonly is created_at and updated_at

@admin.register(BankingDocument)
class BankingDocumentAdmin(admin.ModelAdmin):
    list_display = ['title', 'document_type', 'status', 'customer_name', 'customer_id', 'created_at']
    list_filter = ["document_type", "status"]
    search_fields = ["title", "customer_name", "customer_id"]
    readonly_fields = ["created_at", "updated_at"]

@admin.register(WorkflowTask)
class WorkflowTaskAdmin(admin.ModelAdmin):
    list_display = ['task_type', 'document', 'assigned_to', 'is_completed', 'created_at']
    list_filter = ['task_type', 'is_completed']
    readonly_fields = ['created_at', 'completed_at']