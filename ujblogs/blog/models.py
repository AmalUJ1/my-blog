from django.utils import timezone
from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from autoslug import AutoSlugField

STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('publish', 'Publish'),
    )

class Post(models.Model):  
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at'] 

    def __str__(self):
        return self.title