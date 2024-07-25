from django.urls import path
from .views import ArticleDetailView

urlpatterns = [
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]