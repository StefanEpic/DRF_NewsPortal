from rest_framework import routers
from .views import AuthorViewset, CategoryViewset, UsersViewset, NewsViewset, ArticlesViewset
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', UsersViewset)
router.register(r'author', AuthorViewset)
router.register(r'category', CategoryViewset)
router.register(r'news', NewsViewset, basename='news')
router.register(r'articles', ArticlesViewset, basename='articles')

urlpatterns = [
    path('', include(router.urls)),
]
