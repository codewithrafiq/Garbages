from django.db import models
from django.contrib.gis.db import models

from django.db.models import Manager as GeoManager


class Location(models.Model):
    """
    Location model
    """
    name = models.CharField(max_length=255)
    location = models.PointField()
    objects = GeoManager()

    def __str__(self):
        return self.name



class District(models.Model):
    adm0_en = models.CharField(max_length=50,blank=True,null=True)
    adm0_pcode = models.CharField(max_length=50,blank=True,null=True)
    adm1_en = models.CharField(max_length=50,blank=True,null=True)
    adm1_pcode = models.CharField(max_length=50,blank=True,null=True)
    adm2_en = models.CharField(max_length=50,blank=True,null=True)
    adm2_pcode = models.CharField(max_length=50,blank=True,null=True)
    adm3_en = models.CharField(max_length=50,blank=True,null=True)
    adm3_pcode = models.CharField(max_length=50,blank=True,null=True)
    adm4_en = models.CharField(max_length=50,blank=True,null=True)
    adm4_pcode = models.CharField(max_length=50,blank=True,null=True)
    adm4_ref = models.CharField(max_length=50,blank=True,null=True)
    adm4alt1en = models.CharField(max_length=50,blank=True,null=True)
    adm4alt2en = models.CharField(max_length=50,blank=True,null=True)
    point_x = models.FloatField()
    point_y = models.FloatField()
    geom = models.MultiPointField(srid=4326)

    def __unicode__(self):
        return self.adm0_en


class Country(models.Model):
    fips = models.CharField(max_length=50,blank=True,null=True)
    iso2 = models.CharField(max_length=20,blank=True,null=True)
    iso3 = models.CharField(max_length=30,blank=True,null=True)
    un = models.IntegerField()
    name = models.CharField(max_length=50,blank=True,null=True)
    area = models.IntegerField()
    pop2005 = models.BigIntegerField()
    region = models.IntegerField()
    subregion = models.IntegerField()
    lon = models.FloatField()
    lat = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)