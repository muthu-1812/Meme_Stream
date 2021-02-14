from django.db import models

# Create your models here.
class Meme(models.Model):
    caption=models.CharField(max_length=200)            #caption
    name=models.CharField(max_length=200)
    url=models.URLField(max_length=300)


    def __str__(self):
        return self.url