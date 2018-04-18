from django.db import models


class BaseModel(models.Model):
    """
    Abstract model with auto-increment id and created and updated fields that
    are automatically set and updated.
    """
    id = models.AutoField(primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class RoadSegment(BaseModel):
    coordinates = models.TextField()
    county = models.IntegerField()
    srid = models.IntegerField()
    href = models.CharField(max_length=150)
    category = models.CharField(max_length=4)
    municipality = models.IntegerField()
    startdate = models.DateField()
    region = models.IntegerField()
    status = models.CharField(max_length=4)
    stretchdistance = models.IntegerField()
    typeofroad = models.CharField(max_length=100)
    roadsectionid = models.IntegerField()
    vrefshortform = models.CharField(max_length=255)


class ProductionData(BaseModel):
    time = models.DateTimeField()
    startlat = models.FloatField()
    startlong = models.FloatField()
    endlat = models.FloatField()
    endlong = models.FloatField()
    dry_spreader_active = models.NullBooleanField()
    plow_active = models.NullBooleanField()
    wet_spreader_active = models.NullBooleanField()
    brush_active = models.NullBooleanField()
    material_type_code = models.IntegerField(null=True)
