from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from wissen_app.models import User, Project
from wissen_app.api.serializers import UserSerializer, ProjectSerializer


class ProjectAV(APIView):
    
    def get(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectSerializer(
            project, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        platform = Project.objects.get(pk=pk)
        serializer = ProjectSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        platform = Project.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ProjectDetailAV(APIView):
    def get(self, request):
        project = Project.objects.all()
        serializer = ProjectSerializer(
            project, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def user_details(request, pk):
    if request.method == 'GET':
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    if request.method =='PUT':
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    if request.method == 'DELETE':
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=204)