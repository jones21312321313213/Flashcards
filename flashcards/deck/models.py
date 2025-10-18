from django.db import models

from user.models import User
# Create your models here.
class Deck(models.Model):
    deckId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)