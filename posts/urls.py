from django.urls import path
from posts.views import PostView, PostDetailView, TagView, TagDetailView, AuthorView, AuthorDetailView

urlpatterns = [
    path('', PostView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('tags/', TagView.as_view()),
    path('tags/<int:pk>/', TagDetailView.as_view()),
    path('authors/', AuthorView.as_view()),
    path('authors/<int:pk>/', AuthorDetailView.as_view())
]