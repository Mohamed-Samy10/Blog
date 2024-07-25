from django.shortcuts import render
from .serializers import ArticleSerializer
from .models import Article
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class ArticleDetailView(APIView):
    def get(self, request, slug):
        try:
            article =Article.objects.get(slug=slug)
            serilizer = ArticleSerializer(article)
            return Response(serilizer.data)
        except Article.DoesNotExist:
            return Response ({'message': 'Article not found.'}, status=status.HTTP_404_NOT_FOUND)