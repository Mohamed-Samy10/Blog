from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone




class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
    
class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to='article', null=True, blank=True, default="article/blog.png")
    content = CKEditor5Field(config_name='extends')
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def save(self, *args, **kwargs):
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
        elif self.status == 'draft':
            self.published_at = None
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
    class Meta:
        ordering = ('-published_at',)
        
    def __str__(self):
        return self.title