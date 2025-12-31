from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer
from .auth_middleware import authenticate_request

class TodoListCreate(APIView):
    def get(self, request):
        user = authenticate_request(request)
        todos = Todo.objects.filter(user=user)
        return Response(TodoSerializer(todos, many=True).data)

    def post(self, request):
        user = authenticate_request(request)
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TodoUpdateDelete(APIView):
    def put(self, request, id):
        user = authenticate_request(request)
        try:
            todo = Todo.objects.get(id=id, user=user)
        except:
            return Response({"message": "Not found"}, status=404)

        serializer = TodoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, id):
        user = authenticate_request(request)
        try:
            Todo.objects.get(id=id, user=user).delete()
            return Response({"message": "Todo deleted"})
        except:
            return Response({"message": "Not found"}, status=404)
