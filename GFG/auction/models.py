from django.db import models
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=50)
    description = models.TextField()
    slug = models.SlugField(null=True, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)