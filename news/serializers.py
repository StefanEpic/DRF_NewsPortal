from .models import Author, Category, Post
from django.contrib.auth.models import User
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['user', 'subscribers', ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['theme', 'subscribers', ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['author', 'type', 'date_in', 'category', 'title', 'text', 'image', ]
