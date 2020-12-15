from django.shortcuts import render

from rest_framework import viewsets

from .serializers import PlanSerializer, QuoteSerializer
from .models import Plan, Quote


class PlanViewSet(viewsets.ModelViewSet):
    serializer_class = PlanSerializer

    def get_queryset(self):
        return Plan.objects.all().order_by('id')

    def perform_create(self, serializer):
        # TODO: need this?
        serializer.save()


class QuoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        if 'id' in self.request.query_params.keys():
            return Quote.objects.filter(id=self.request.query_params['id'])\
                .all().order_by('id')
        else:
            return Quote.objects.all().order_by('id')

    def perform_create(self, serializer):
        # TODO: finish
        serializer.save()

