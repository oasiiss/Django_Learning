from django.urls import path, include
from posts.views import PostViewSet, AuthorViewSet, TagViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('authors', AuthorViewSet)
router.register('tags', TagViewSet)

urlpatterns = [
    path('', include(router.urls))
]