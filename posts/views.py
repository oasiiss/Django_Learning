from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from posts.models import Post, Tag, Author
from posts.serializers import TagSerializer, AuthorSerializer, PostSerializer

# Create your views here.
class PostView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class TagView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer  

class TagDetailView(generics.RetrieveDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class AuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetailView(generics.RetrieveDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer