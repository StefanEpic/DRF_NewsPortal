from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import AuthorSerializer, CategorySerializer, UsersSerializer, PostSerializer
from .models import Author, Category, Post


class UsersViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NewsViewset(viewsets.ModelViewSet):
    queryset = Post.objects.filter(type='news')
    serializer_class = PostSerializer


class ArticlesViewset(viewsets.ModelViewSet):
    queryset = Post.objects.filter(type='arti')
    serializer_class = PostSerializer
