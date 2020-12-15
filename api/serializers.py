from rest_framework import serializers

from .models import Plan, Quote


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('id',
                  )


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('id',
                  'quote_number',
                  'effective_date',
                  'previous_policy_cancelled',
                  'property_mileage_to_nearest_volcano',
                  'owns_property_to_be_insured',
                  'mailing_address',
                  'property_address',
                  'plan_id',
                  )
