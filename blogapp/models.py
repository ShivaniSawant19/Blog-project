from django.db import models
from django.contrib.auth.models import User

class Add_Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', blank = True, null = True)
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __self__(self):
        return self.title[:50]
