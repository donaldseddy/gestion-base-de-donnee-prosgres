from django.db import models
from django.contrib.gis.db.models import PointField
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.contrib.gis.db import models as gis_models

# Create your models here.


"create a model for blog produit with the following fields: name, ref, description, price, latitude, longitude, longitude, geolocalization, created_at, updated_at"
class BlogProduit(models.Model):
    name = models.CharField(max_length=255)
    ref = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    latitude = models.FloatField()
    longitude = models.FloatField()
    geolocalization = models.PointField(geography=True, srid=4326, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
