from django.shortcuts import render
from django.core.exceptions import ValidationError

from rest_framework import viewsets, mixins

from .serializers import PlanSerializer, QuoteSerializer
from .models import Plan, Quote


class PlanViewSet(mixins.RetrieveModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = PlanSerializer

    def get_queryset(self):
        try:
            if 'id' in self.request.query_params.keys():
                return Plan.objects.filter(id=self.request.query_params['id'])\
                    .all().order_by('id')
            else:
                return Plan.objects.all().order_by('id')
        except ValidationError as e:
            # Bad UUID was used to request, just return empty.
            return None


class QuoteViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer

    def get_queryset(self):
        try:
            if 'id' in self.request.query_params.keys():
                return Quote.objects.filter(id=self.request.query_params['id'])\
                    .all().order_by('id')
            else:
                # Removed because it's not a requirement to return all quotes
                return None
                # return Quote.objects.all().order_by('id')
        except ValidationError as e:
            # Bad UUID was used to request, just return empty.
            return None

    def perform_create(self, serializer):
        serializer.save()

