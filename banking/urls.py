from django.urls import path
from . import views

#namespace
app_name = "banking"

urlpatterns = [
    path('', views.document_list, name="document_list"),
    path('documents/upload', views.document_form_upload, name="document_upload"),
    path('documents/<pk>/', views.document_detail, name="document_detail"),
    path('tasks/', views.workflow_tasks, name="workflow_tasks"),
    path('tasks/<pk>/complete/', views.complete_task, name="complete_task"),
]