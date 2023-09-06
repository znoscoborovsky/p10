from rest_framework import serializers
from .models import Projects, Issues, Comments

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = ['id', 'title', "description", "type", "author", "created_time"]

class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issues
        fields = ['id',"title" ,'project', "created_time", "description", "status",
                  "priority", "balise", "assignee_user"]

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ['id','title' ,'issue', "description", "author", "created_time"]