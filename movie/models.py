from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.TextField()
    completed = models.BooleanField(default=True)
    
    
    class Meta:
        db_table = 'movie'