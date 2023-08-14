from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Phone(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.name}: {self.price}, {self.release_date}, {self.lte_exists}'


    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})
