from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscribers = models.ManyToManyField(
        User, blank=True, related_name='authors')

    def __str__(self):
        return self.user.username


class Category(models.Model):
    theme = models.CharField(max_length=50, unique=True)
    subscribers = models.ManyToManyField(
        User, blank=True, related_name='categories')

    def __str__(self):
        return self.theme


class Post(models.Model):
    news = 'news'
    arti = 'arti'

    TYPES = [
        (news, 'News'),
        (arti, 'Articles')
    ]

    author = models.ForeignKey(
        Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=4, choices=TYPES,
                            default=news)
    date_in = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to='post_images/%Y/%m/%d/', blank=True)

    def __str__(self):
        return f'{self.author.user.username} / {self.title}'
