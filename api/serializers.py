from rest_framework import serializers

from .models import Plan, Quote, Address, Variable


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('line1', 'city', 'state', 'zip_code')


class QuoteSerializer(serializers.ModelSerializer):
    mailing_address = AddressSerializer(read_only=True)
    property_address = AddressSerializer(read_only=True)

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


class VariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variable
        fields = ('name', 'description', 'value')


class PlanSerializer(serializers.ModelSerializer):
    plan_variables = VariableSerializer(many=True, read_only=True)

    class Meta:
        model = Plan
        fields = ('id',
                  'name',
                  'plan_variables'
                  )



