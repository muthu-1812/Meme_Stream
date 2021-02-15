from django.db import models


#REPRESENTS THE OBJECTS IN THE DATABASE
#MODEL FOR THE MEME TO MAKE EASIER CHANGES TO THE DB
#MAKES SURE TO MIGRATE AFTER MAKING CHANGES
class Meme(models.Model):
    caption=models.CharField(max_length=200)            
    name=models.CharField(max_length=200)
    url=models.URLField(max_length=300)


    def __str__(self):
        return self.url