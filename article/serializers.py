from rest_framework import serializers
from .models import Article,Category,Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    tags = TagSerializer(many=True)
    class Meta:
        model = Article
        fields = 'title', 'slug', 'image', 'content', 'created_at','published_at', 'updated_at', 'status', 'category', 'tags'