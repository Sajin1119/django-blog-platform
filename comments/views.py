from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer
from posts.models import Post


class PostCommentListCreateView(generics.ListCreateAPIView):

    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id, parent=None)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = Post.objects.get(id=post_id)

        serializer.save(
            author=self.request.user,
            post=post
        )


class CommentDeleteView(generics.DestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]