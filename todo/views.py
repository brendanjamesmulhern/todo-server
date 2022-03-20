from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, ToDoSerializer
from rest_framework import status
from django.contrib.auth.models import User
from .models import Item
from django.contrib.auth import authenticate

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'Register': '/api/register',
        'Login User': '/api/login',
        'List': '/api/todos/',
        'Create': '/api/todos/create/',
        'Update': '/api/todos/<int:pk>/update/',
        'Delete': '/api/todos/<int:pk>/delete/',
    }
    return Response(api_urls)

@api_view(['POST'])
def register(request):
    new_user = UserSerializer(data=request.data)
    if new_user.is_valid():
        new_user.save()
        return Response(new_user.data, status=status.HTTP_201_CREATED)
    return Response(new_user.errors)

@api_view(['POST'])
def login(request):
    user = User.objects.get(username=request.data['username'])
    if user:
        if user.password == request.data['password']:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_todo(request):
    todo = ToDoSerializer(data=request.data)
    if todo.is_valid():
        todo.save()
        return Response(todo.data, status=status.HTTP_201_CREATED)
    else:
        return Response(todo.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_one_todo(request):
    items = Item.objects.all()
    serializer = ToDoSerializer(items, many=True)
    return Response(serializer.data)
    
   
@api_view(['POST'])
def update_todo(request, pk):
    item = Item.objects.get(pk=pk)
    data = ToDoSerializer(instance=item, data=request.data)

    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def delete_todo(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



