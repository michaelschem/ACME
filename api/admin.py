from django.contrib import admin

from .models import Plan, Quote, Address, Variable, \
    ProximityToVolcano, UnderwaterVolcanoCoverage, SuperVolcanoCoverage, CoverageLimit, \
    Premium, Tax, ConvenienceFee

admin.site.register(Plan)
admin.site.register(Quote)
admin.site.register(Address)
# admin.site.register(Variable)
admin.site.register(ProximityToVolcano)
admin.site.register(UnderwaterVolcanoCoverage)
admin.site.register(SuperVolcanoCoverage)
admin.site.register(CoverageLimit)
admin.site.register(Premium)
admin.site.register(Tax)
admin.site.register(ConvenienceFee)
