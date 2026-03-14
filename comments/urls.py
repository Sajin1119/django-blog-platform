from django.urls import path
from .views import PostCommentListCreateView, CommentDeleteView

urlpatterns = [
    path('post/<int:post_id>/', PostCommentListCreateView.as_view(), name="post-comments"),
    path('delete/<int:pk>/', CommentDeleteView.as_view(), name="delete-comment"),
]