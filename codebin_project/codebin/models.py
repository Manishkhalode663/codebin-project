from django.db import models

# Create your models here.
class Snippet(models.Model):
    title = models.CharField(max_length=200 )
    code = models.TextField()
    language = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    
    
