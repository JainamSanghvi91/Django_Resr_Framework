from django.conf.urls import url
from cars.api.views import CarsAPIView

urlpatterns = [
    url('car', CarsAPIView.as_view())
]
