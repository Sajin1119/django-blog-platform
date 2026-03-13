from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [

    path('', PostListView.as_view()),

    path('create/', PostCreateView.as_view()),

    path('update/<int:pk>/', PostUpdateView.as_view()),

    path('delete/<int:pk>/', PostDeleteView.as_view()),
    
    path('<slug:slug>/', PostDetailView.as_view()),

]