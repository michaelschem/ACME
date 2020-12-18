from rest_framework import serializers

from .models import Plan, Quote, Address, Variable


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('line1', 'city', 'state', 'zip_code')


class QuoteSerializer(serializers.ModelSerializer):
    mailing_address = AddressSerializer(read_only=False)
    property_address = AddressSerializer(read_only=False)

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
                  'plan',
                  )

    def create(self, validated_data):
        mailing_address_data = validated_data.pop('mailing_address')
        mailing_address = Address.objects.create(**mailing_address_data)

        property_address_data = validated_data.pop('property_address')
        property_address = Address.objects.create(**property_address_data)

        quote = Quote.objects.create(mailing_address=mailing_address, property_address=property_address, **validated_data)

        return quote


class VariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variable
        fields = ('name', 'description', 'value')


class PlanSerializer(serializers.ModelSerializer):
    plan_variables = serializers.SerializerMethodField('collect_plan_variables')
    rate_variables = serializers.SerializerMethodField('collect_rate_variables')

    def collect_plan_variables(self, plan):
        return [VariableSerializer(plan.proximity_to_volcano).data,
                VariableSerializer(plan.underwater_volcano_coverage).data,
                VariableSerializer(plan.super_volcano_coverage).data,
                VariableSerializer(plan.coverage_limit).data]

    def collect_rate_variables(self, plan):
        return [VariableSerializer(plan.premium).data,
                VariableSerializer(plan.tax).data,
                VariableSerializer(plan.convenience_fee).data]

    class Meta:
        model = Plan
        fields = ('id',
                  'name',
                  'plan_variables',
                  'rate_variables',
                  )

# class PlanSerializer(serializers.Serializer):
#     name = serializers.CharField()
#     proximity_to_volcano = VariableSerializer()
#     # plan_variables = serializers.ListField()


