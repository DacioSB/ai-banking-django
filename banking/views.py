from django.shortcuts import render
from django.http.request import HttpRequest

from banking.models import BankingDocument
# Create your views here.

#cria a funcao document_list recebendo o request
# vai no bankingdocuments pega todos
#pega do request get, o atributo type e o atributo status
# se houver type, filtra a lista de documentos pelo type
# se houver staus, filtra pelo status

# criar um dicionario com o contexto contendo: documents obvio, document_types, status_choices, current_type e current_status
# passa tudo no retorno do render request, a pagina html e o contexto

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
