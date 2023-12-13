from django.db import models

# Create your models here.
class Note(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=256)
    done = models.BooleanField(default=False)
    title = models.CharField(max_length=64)
    
    
    def checking(self):
        self.done = True
        self.save()
    
    def __str__(self):
	    return self.description