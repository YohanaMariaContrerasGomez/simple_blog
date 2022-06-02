from django.db import models

from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from categories.models import Category

class Post(models.Model):
    """Post Model."""

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    profile = models.ForeignKey('Users.profile', on_delete=models.PROTECT)

    title = models.CharField(max_length=255)
    image_header = models.ImageField(upload_to = 'posts/photos')
    post = RichTextField()

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    url = models.SlugField(max_length=255, unique=True)
    views = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ('Title',)

    def __str__(self):
        """Return title and username"""
        return '{} by @{}'.format(self.title, self.user.username)

    def save(self, *args, **kwargs):
        self.url = slugify(self.title)
        super(Post, self).save(*args, **kwargs)   