from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from posts.models import Post, Tag, Author
from posts.serializers import TagSerializer, AuthorSerializer, PostSerializer

# Create your views here.

class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()

        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)

class TagView(APIView):
    def get(self, request):
        tags = Tag.objects.all()

        serializer = TagSerializer(tags, many=True)

        return Response(serializer.data)
    
class AuthorView(APIView):
    def get(self, request):
        authors = Author.objects.all()

        serializer = AuthorSerializer(authors, many=True)

        return Response(serializer.data)