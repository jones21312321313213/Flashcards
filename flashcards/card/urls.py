from django.urls import path
from .views import AnswerCardView, ReviewDeckView

urlpatterns = [
    # The URL pattern is the same, but the view is now a class
    path('review/<int:deck_id>/', ReviewDeckView.as_view(), name='review_deck'),
    path('answer/<int:card_id>/', AnswerCardView.as_view(), name='answer_card'),
]