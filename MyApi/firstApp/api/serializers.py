from rest_framework import serializers
from firstApp.models import CarSpecs

class CarSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecs
        fields = ['id', 'car_plan', 'car_brand','car_model','production_year','car_body','engine_type']
        depth=1 # Depth=1 means that this will not ol=nly display the foreign key value but also all values of that model in this case in CarSpec it will display all the values of CarPlan model.