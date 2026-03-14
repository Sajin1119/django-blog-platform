from rest_framework import serializers
from .models import Post, Category, Tag


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']
from rest_framework import serializers
from .models import Post

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post._meta.get_field('author').related_model  # User model
        fields = ['id', 'username']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)  # nested author
    tags = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')
    category = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'content', 'image',
            'author', 'category', 'tags',
            'created_at', 'updated_at',
            'views_count', 'is_published'
        ]