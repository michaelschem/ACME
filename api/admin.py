from django.contrib import admin

from .models import Plan, Quote, Address, Variable, \
    ProximityToVolcanoPlanVariable, UnderwaterVolcanoCoveragePlanVariable, SuperVolcanoCoveragePlanVariable, CoverageLimitPlanVariable, \
    PremiumRateVariable, TaxRateVariable, ConvenienceFeeRateVariable

admin.site.register(Plan)
admin.site.register(Quote)
admin.site.register(Address)
# admin.site.register(Variable)
admin.site.register(ProximityToVolcanoPlanVariable)
admin.site.register(UnderwaterVolcanoCoveragePlanVariable)
admin.site.register(SuperVolcanoCoveragePlanVariable)
admin.site.register(CoverageLimitPlanVariable)
admin.site.register(PremiumRateVariable)
admin.site.register(TaxRateVariable)
admin.site.register(ConvenienceFeeRateVariable)
