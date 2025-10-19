from django.urls import path
from . import views

urlpatterns = [
    #Deck
    path('list/add', views.DeckCreateView.as_view(), name='deck_add'),
    path('list', views.DeckListView.as_view(), name='deck_list'),
    path('list/deck<int:pk>', views.DeckUpdateView.as_view(), name='deck_view'),
]