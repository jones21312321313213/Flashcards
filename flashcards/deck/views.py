from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
#Deck
class DeckCreateView(View):
    template_name = 'todo'

    def get(self, request):
        return HttpResponse('creating deck')

class DeckListView(View):
    template_name = 'todo'

    def get(self, request):
        return HttpResponse('list of deck')
class DeckUpdateView(View):
    template_name = 'todo'

    def get(self, request, pk):
        return HttpResponse(f'Viewing deck {pk}')
