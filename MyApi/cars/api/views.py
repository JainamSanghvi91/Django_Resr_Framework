from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from cars.models import Cars
from cars.api.serializes import CarSerializer

class CarsAPIView(APIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        car = Cars.objects.all()
        return car

    def get(self, request, *args, **kwargs):
        try:
            # this is used to get the specific id data means "?id=2" this means id with 2 is only required data.
            id = request.query_params["id"]
            print(id)
            if id != None:
                car = Cars.objects.get(id=id)
                serializer = CarSerializer(car)
        except:
            cars = self.get_queryset()
            serializer = CarSerializer(cars, many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        car_data = request.data
        # This is the instance of CarPlan model and we are using this as foreign key in CarSpec and thus we are fetching the id here.
        # Create object to use POST API and send this object containing all data.
        new_car = Cars.objects.create(car_brand=car_data["car_brand"],car_model=car_data["car_model"],production_year=car_data["production_year"],car_body=car_data["car_body"],engine_type=car_data["engine_type"],)
        new_car.save()
        # We got all the data into object and saved it now, we will serialize our data to send the data
        serialize = CarSerializer(new_car)
        return Response(serialize.data)

    