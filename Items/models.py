from django.db import models

# Create your models here.

class all_images(models.Model):
    name_images = models.CharField(max_length=500)
    json_imagess = models.JSONField()

    def __str__(self):
        return  self.name_images