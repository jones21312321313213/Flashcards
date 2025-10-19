from django.http import HttpResponse
from django.views import View


class ReviewDeckView(View):
    def get(self, card):
        return HttpResponse(f'Card: {card}')

    def get_specific_card(self, card):
        return HttpResponse(f'Card: {card}')

    def get_template_for_card(self, card):
        if hasattr(card, 'basiccard'):
            return HttpResponse('basic card')
        if hasattr(card, 'identificationcard'):
            return HttpResponse('identifation card')
        if hasattr(card, 'imageocclusioncard'):
            return HttpResponse('image occlusion card')
        return HttpResponse('basic card')


class AnswerCardView(View):
    def post(self, card):
        return HttpResponse('Answering card')