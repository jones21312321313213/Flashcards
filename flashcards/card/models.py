from django.db import models

from user.models import User
from deck.models import Deck
# Create your models here.
class Card(models.Model):
    #card_type = (('B','Basic'),('I','Identification','IO','ImageOcclusion')) add this if needed
    cardId = models.AutoField(primary_key=True) # or use cardId = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    next_review = models.DateTimeField(auto_now=True)
    input_field = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

    def __str__(self):
        return self.card_type + " " + self.cardId + " " + self.created_at + " " + self.next_review + " " + self.input_field

class Basic(Card):
    back_field = models.CharField(max_length=200)

    def __str__(self):
        return self.back_field

class Identification(Card):
    hidden_field = models.CharField(max_length=200)

    def __str__(self):
        return self.hidden_field

class ImageOcclusion(Card):
    img_path = models.CharField(max_length=200)

    def __str__(self):
        return self.img_path

