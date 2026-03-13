from django.urls import path
from .views import PostCommentListCreateView, CommentDeleteView

urlpatterns = [

    path('post/<int:post_id>/', PostCommentListCreateView.as_view()),

    path('delete/<int:pk>/', CommentDeleteView.as_view()),

]