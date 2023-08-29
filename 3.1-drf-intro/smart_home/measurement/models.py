from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255, null=True)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, verbose_name='Датчик')
    temperature = models.IntegerField(verbose_name="Температура")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время изменения")