from django.db import models

# Create your models here.

class Images(models.Model):
    images = models.ImageField(upload_to="gallery")
    date = models.DateTimeField(auto_now_add=True)