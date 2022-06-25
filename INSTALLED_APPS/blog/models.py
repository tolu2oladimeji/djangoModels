from django.db import models

# Create your models here.

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    #Author= get_user_model()
    Created_date = models.DateTimeField()
    Published_date =models.DateTimeField()
