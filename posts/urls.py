from django.urls import path
from posts.views import PostView, TagView

urlpatterns = [
    path('', PostView.as_view()),
    path('tags/', TagView.as_view())
]