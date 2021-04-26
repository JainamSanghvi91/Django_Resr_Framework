from django.db import models

# Create your models here.

class CarPlan(models.Model):
    plan_name = models.CharField(max_length=20)
    years_of_warranty = models.PositiveIntegerField(default=1)
    finanace_plan = models.CharField(max_length=20, default="unavailable")

    # This function helps us to change the name in the admin site of the objects of CarPlan added and keep name as plan_name name.
    def __str__(self):
        return self.plan_name

class CarSpecs(models.Model):
    car_plan = models.ForeignKey(CarPlan, on_delete=models.SET_NULL, null=True, default=1)
    car_brand = models.CharField(max_length=50)
    car_model = models.CharField(max_length=100)
    production_year = models.CharField(max_length=10)
    car_body = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=50)

    # This function helps us to change the name in the admin site of the objects of Carspecs added and keep name as car_brand name.
    def __str__(self):
        return self.car_brand
    
