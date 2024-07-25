from django.contrib import admin
from .models import Category,Tag,Article
admin.site.register(Category)
admin.site.register(Tag)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug',)
    prepopulated_fields = {'slug': ('title',), }
