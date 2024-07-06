from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post, Tag

# Create your views here.

class PostView(APIView):
    def get(self, request):
        posts_title = [post.title for post in Post.objects.all()]

        return Response(posts_title)

class TagView(APIView):
    def get(self, request):
        tags = Tag.objects.all()

        return Response(tags)