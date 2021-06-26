from django.db import models

# Create your models here.

class Doc(models.Model):
    upload = models.FileField(upload_to='text/')
    name = models.CharField(max_length = 15, default = "notes")
    def __str__(self):
        return str(self.pk)