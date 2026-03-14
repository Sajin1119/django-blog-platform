from rest_framework import generics, permissions,filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post,PostLike
from .serializers import PostSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class PostListView(generics.ListAPIView):
    queryset = Post.objects.filter(is_published=True).order_by('-created_at')
    serializer_class = PostSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ['category']
    search_fields = ['title', 'content']


class PostDetailView(generics.RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()

        instance.views_count += 1
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PostCreateView(generics.CreateAPIView):

    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostUpdateView(generics.UpdateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

class PostDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    lookup_field = 'slug'



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):

    post = Post.objects.get(id=post_id)

    like, created = PostLike.objects.get_or_create(
        user=request.user,
        post=post
    )

    if not created:
        like.delete()
        return Response({"message": "Post unliked"})

    return Response({"message": "Post liked"})


@api_view(['GET'])
def post_likes(request, post_id):

    post = Post.objects.get(id=post_id)

    likes_count = post.likes.count()

    return Response({
        "post": post_id,
        "likes": likes_count
    })