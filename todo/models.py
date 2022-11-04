from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField(max_length=300)
    done = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title