from django.db import models

# Create your models here.


class User(models.Model):
    userId = models.AutoField(primary_key=True) # or userId = models.IntegerField(primary_key=True) choose which is correct
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length= 100)# or email = models.EmailField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.userId} {self.username} {self.email}"