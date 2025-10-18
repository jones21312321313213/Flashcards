from django.db import models

from user.models import User
from card.models import Card

class Notification(models.Model):
    notificationId = models.AutoField(primary_key=True)
    description = models.CharField(max_length=128)
    status = models.BooleanField(default=False)
    schedule = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.notificationId} {self.description} {self.status} {self.schedule} {self.user.username} {self.card.cardId}"
