from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer
from .auth_middleware import authenticate_request

@api_view(['GET', 'POST'])
def todo_list_create(request):
    user = authenticate_request(request)
    if request.method == 'GET':
        todos = Todo.objects.filter(user=user)
        return Response(TodoSerializer(todos, many=True).data)

    # POST
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def todo_update_delete(request, id):
    user = authenticate_request(request)
    if request.method == 'PUT':
        try:
            todo = Todo.objects.get(id=id, user=user)
        except Todo.DoesNotExist:
            return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    try:
        Todo.objects.get(id=id, user=user).delete()
        return Response({"message": "Todo deleted"})
    except Todo.DoesNotExist:
        return Response({"message": "Not found"}, status=status.HTTP_404_NOT_FOUND)
