from django.db import models

class Word(models.Model):
    text = models.CharField(max_length=120)

    def __str__(self):
        return self.text
    

