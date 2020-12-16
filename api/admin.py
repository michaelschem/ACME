from django.contrib import admin

from .models import Plan, Quote, Address, Variable, \
    IntPlanVariable, StrPlanVariable, FltPlanVariable, BoolPlanVariable, \
    IntRateVariable, StrRateVariable, FltRateVariable, BoolRateVariable

admin.site.register(Plan)
admin.site.register(Quote)
admin.site.register(Address)
admin.site.register(Variable)
admin.site.register(IntPlanVariable)
admin.site.register(StrPlanVariable)
admin.site.register(FltPlanVariable)
admin.site.register(BoolPlanVariable)
admin.site.register(IntRateVariable)
admin.site.register(StrRateVariable)
admin.site.register(FltRateVariable)
admin.site.register(BoolRateVariable)
