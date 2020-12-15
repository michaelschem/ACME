from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'plan', views.PlanViewSet, basename='PlanViewSet')
router.register(r'quote', views.QuoteViewSet, basename='QuoteViewSet')

urlpatterns = [
    path('', include(router.urls)),
]