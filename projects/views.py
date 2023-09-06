from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProjectSerializer, IssueSerializer, CommentSerializer
from .models import Projects, Issues, Comments
from rest_framework.decorators import api_view

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    #permission_classes = [permissions.IsAuthenticated]

class IssueViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Issues.objects.all()
    serializer_class = IssueSerializer
    #permission_classes = [permissions.IsAuthenticated]

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    #permission_classes = [permissions.IsAuthenticated]
