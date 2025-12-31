from django.urls import path
from .views import todo_list_create, todo_update_delete

urlpatterns = [
    path('', todo_list_create),
    path('<int:id>/', todo_update_delete),
]
