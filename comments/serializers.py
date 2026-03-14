from rest_framework import serializers
from .models import Comment
from users.serializers import AuthorSerializer



class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # 👈 change from ReadOnlyField to nested

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'parent', 'content', 'created_at']
        read_only_fields = ['author', 'post']