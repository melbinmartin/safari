
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="pics/docs/",
                              default="pics/default_post.jpg")
    desc = models.TextField(blank=False,max_length=300)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):

        super().save(force_insert, force_update, using, update_fields)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
