from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField
    likes = models.IntegerField(default=0)
    verified = models.BooleanField(default=False)
    added_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField()