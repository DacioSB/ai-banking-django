from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.http.request import HttpRequest
from django.utils import timezone

from banking.forms import DocumentUploadForm
from banking.models import BankingDocument, WorkflowTask

def document_list(request: HttpRequest):
    documents = BankingDocument.objects.all()
    type = request.GET.get("type")
    status = request.GET.get("status")

    if type:
        documents = documents.filter(type)
    if status:
        documents = documents.filter(status)

    context = {
        "documents": documents,
        "document_types": BankingDocument.DOCUMENT_TYPES,
        "status_choices": BankingDocument.STATUS_CHOICES,
        "current_type": type,
        "current_status": status
    }
    return render(request=request, template="banking/document_list.html", context=context)

#document_form_upload
def document_form_upload(request: HttpRequest):
    if request.method == "POST":
        form = DocumentUploadForm(request.POST)
        if form.is_valid():
            document = form.save(commit=False)
            document.save()
            _create_workflow_tasks(document)
            messages.success(request, f'Document "{document.title}" uploaded successfully.')
            return redirect("banking:document_list")
    else:
        form = DocumentUploadForm()
    return render(request, "banking/document_upload.html", {"form": form})

# document_detail receives the request and the pk
#get or 404 in BankingDocument and pk
#get all tasks from the document
#return a render of banking/document_detail.html passing the document and the tasks separetely
def document_detail(request, pk):
    document = get_object_or_404(BankingDocument, pk)
    tasks = document.tasks.all()
    return render(request, "banking/document_detail.html", {
        "document": document,
        "tasks": tasks
    })

def workflow_tasks(request):
    tasks = WorkflowTask.objects.filter(is_completed=False)
    return render(request, 'banking/workflow_tasks.html', {'tasks': tasks})

def complete_task(request, pk):
    task = get_object_or_404(WorkflowTask, pk)
    task.is_completed = True
    task.completed_at = timezone.now()
    task.save()
    messages.success(request, f'Task "{task.get_task_type_display()}" marked as completed.')
    return redirect("banking:workflow_tasks")


def _create_workflow_tasks(document):
    """Generate placeholder workflow tasks based on the document type."""
    task_map = {
        'loan_application': [
            ('document_review', 'Review loan application documents for completeness'),
            ('risk_assessment', 'Conduct risk assessment for loan applicant'),
            ('approval_request', 'Submit for final approval'),
        ],
        'kyc': [
            ('document_review', 'Verify identity documents'),
            ('compliance_check', 'Run compliance and AML checks'),
        ],
        'compliance': [
            ('compliance_check', 'Review compliance report and flag issues'),
        ],
        'account_statement': [
            ('document_review', 'Review account statement for anomalies'),
        ],
        'risk_assessment': [
            ('risk_assessment', 'Validate risk assessment methodology'),
            ('approval_request', 'Route to risk committee for approval'),
        ],
    }
    for task_type, description in task_map.get(document.document_type, []):
        WorkflowTask.objects.create(
            document=document,
            task_type=task_type,
            description=description,
        )