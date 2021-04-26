from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from firstApp.api.views import firstFunction
from rest_framework.routers import DefaultRouter
from firstApp.api.views import CarSpecsViewset

router = DefaultRouter()
router.register('car-specs', CarSpecsViewset, basename='car-specs')

urlpatterns = [
    url('first/', firstFunction),
    url('',include(router.urls))
]