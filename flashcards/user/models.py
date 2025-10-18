from django.db import models

# Create your models here.


class User(models.Model):
    userId = models.AutoField(primary_key=True) # or userId = models.IntegerField(primary_key=True) choose which is correct
    username = models.CharField(max_length=100,null = False)
    password = models.CharField(max_length=50,null = False)
    email = models.TextField(max_length=100,null = False)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.userId + " " + self.username + " " + self.password + " " + self.email + " " + self.created_at