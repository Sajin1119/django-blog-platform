from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

from .views import like_post, post_likes

urlpatterns = [

    path('', PostListView.as_view()),

    path('create/', PostCreateView.as_view()),

    # DETAIL PAGE
    path('<slug:slug>/', PostDetailView.as_view()),

    path('update/<int:pk>/', PostUpdateView.as_view()),
    path('delete/<slug:slug>/', PostDeleteView.as_view()),
    path('<int:post_id>/like/', like_post),
    path('<int:post_id>/likes/', post_likes),

]