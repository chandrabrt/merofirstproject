from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.urlresolvers import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    p_language = models.CharField(max_length=30, default='Django Tutorial')
    image = models.ImageField(null=False)
    description = models.TextField(max_length=100)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,
                            unique=True)
    author = models.ForeignKey(User, related_name='blog_posts')
    content = RichTextField(default='write something!!........')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='publish')

    def get_absolute_url(self):
        return reverse('blog:blog_index')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField()
    comment = models.TextField(max_length=500)
    post = models.ForeignKey(Post)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_on',)

    def __str__(self):
        return self.comment
