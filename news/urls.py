from rest_framework import routers
from .views import AuthorViewset, CategoryViewset, PostViewset
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'author', AuthorViewset)
router.register(r'category', CategoryViewset)
router.register(r'post', PostViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]