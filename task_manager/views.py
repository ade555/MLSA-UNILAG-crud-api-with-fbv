from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from .models import Task
from .serializers import TaskSerializer
from .paginators import TaskPaginator

# pagination next class
# slugs
@api_view(['POST', 'GET'])
def task_list_view(request):
    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        paginator = TaskPaginator()
        tasks = Task.objects.all()

        # perform search
        query = request.GET.get('q', '')

        # if query:
        #     tasks = Task.objects.filter(task_name=query)
        
        if query:
            tasks = tasks.filter(Q(task_name__icontains=query))

        result = paginator.paginate_queryset(tasks, request)
        serializer = TaskSerializer(result, many=True)
        # return Response(serializer.data)
        return paginator.get_paginated_response(serializer.data)




@api_view(["GET", "PUT", "DELETE"])
def task_detail(request, task_id):
    task = Task.objects.get(pk=task_id)

    if request.method == "GET":
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == "PUT":
        serializer = TaskSerializer(task, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)