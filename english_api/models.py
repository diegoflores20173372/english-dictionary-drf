from django.db import models


# Create your models here.
class Word(models.Model):
    title = models.CharField(max_length=255, unique=True)
    meanings = models.TextField(default="Ipsum Lorem")
    examples = models.TextField(default="Ipsum Lorem")

    def __str__(self):
        return self.title
