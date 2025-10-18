from django.db import models

from flashcards.card.models import Card
from flashcards.user.models import User


# Create your models here.
class Notification(models.Model):
    notificationId = models.AutoField(primary_key=True)
    description = models.CharField(max_length=128)
    status = models.BooleanField(default=False)
    schedule = models.DateTimeField(auto_now_add=True)#can remove the auto_now_add if not needed
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)


    def __str__(self):
        return self.notificationId + " " + self.description + " " + self.status + " "  + self.schedule + " " + self.user + " " + self.card
