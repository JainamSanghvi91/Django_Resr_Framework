# Generated by Django 3.2 on 2021-04-24 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0010_remove_carspecs_car_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='carspecs',
            name='car_plan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='firstApp.carplan'),
        ),
    ]