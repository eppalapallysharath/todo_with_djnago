from django.urls import path
from .views import TodoListCreate, TodoUpdateDelete

urlpatterns = [
    path('', TodoListCreate.as_view()),
    path('<int:id>/', TodoUpdateDelete.as_view()),
]
