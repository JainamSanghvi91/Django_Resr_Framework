from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from firstApp.api.serializers import CarSpecsSerializer
from firstApp.models import CarSpecs,CarPlan

@api_view()
@permission_classes([AllowAny])
def firstFunction(request):
    # This will tell us about the different parameters used in API as key and values and we can perform operations on that key value pairs.
    print(request.query_params)
    print(request.query_params['id'])
    num = request.query_params['id']
    new_num = int(request.query_params['id']) * 2
    return Response({'message' : "We recieved your request", 'result' : new_num})


class CarSpecsViewset(viewsets.ModelViewSet):
    serializer_class = CarSpecsSerializer

    def get_queryset(self):
        car_specs = CarSpecs.objects.all()
        return car_specs

    # def retrieve(self, request, *args, **kwargs):
    #     params = kwargs
    #     print(params['pk'])
    #     # If we have multiple params thene we have to split the parameters as:
    #     params_list = params['pk'].split('-')
    #     cars = CarSpecs.objects.filter(car_brand = params_list[0], car_model=params_list[1]) #This will get all the cars as the parameter we given in the url as per car_brand.
    #     serializer = CarSpecsSerializer(cars, many=True) #This is to serialize all of filtered cars and this will take many common cars as well. 
    #     return Response(serializer.data)   

    # # Also, in this function we all can check that if the created object is already present or not so that we can't repeat the same data.
    # def create(self, request, *args, **kwargs):
    #     car_data = request.data
    #     # This is the instance of CarPlan model and we are using this as foreign key in CarSpec and thus we are fetching the id here.
    #     instance_carplan_fk = CarPlan.objects.get(id=car_data["car_plan"])
    #     # Create object to use POST API and send this object containing all data.
    #     new_car = CarSpecs.objects.create(car_plan=instance_carplan_fk,car_brand=car_data["car_brand"],car_model=car_data["car_model"],production_year=car_data["production_year"],car_body=car_data["car_body"],engine_type=car_data["engine_type"],)
    #     new_car.save()
    #     # We got all the data into object and saved it now, we will serialize our data to send the data
    #     serialize = CarSpecsSerializer(new_car)
    #     return Response(serialize.data)

    # def destroy(self, request, *args, **kwargs):
    #     loggedin_user = request.user
    #     if loggedin_user == "admin":
    #         car = self.get_object()
    #         car.delete()
    #         response_message = {"message" : "Item has been deleted"}
    #     else :
    #         response_message = {"message" : "Not Allowed"}

    #     return Response(response_message)