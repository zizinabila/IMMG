from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.utils.text import slugify
from ckeditor.fields import RichTextField




class Category(models.Model):
    category_code = models.CharField(max_length=20)
    category_desc = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, editable=False)

    def __str__(self):
        return u'{0}'.format(self.category_desc)

    def save(self):
        self.slug = slugify(self.category_desc)
        super().save()

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    content = RichTextField()
    image = models.ImageField(default='default_content.jpg', upload_to='content_pics')
    is_posted = models.BooleanField(default=False)
    date_posted = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='updated_by')
    slug = models.SlugField(blank=True, editable=False)
    
    def __str__(self):
        return "{} .{}".format(self.id, self.title)

    def save(self):
        self.slug = slugify(self.title)
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
