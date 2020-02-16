from django.db import models
from django_mysql.models import ListCharField
from languages.fields import LanguageField
from django_mysql.models import ListTextField
import jsonfield






class Excursion(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    detailPageName = models.CharField(max_length=100)
    portID = models.CharField(max_length=8)
    type = models.CharField(max_length=30)
    typology = jsonfield.JSONField()
    activityLevel = models.CharField(max_length=30)
    collectionType = models.CharField(max_length=30)
    duration  = models.CharField(max_length=200)
    language = jsonfield.JSONField()
    priceLevel = models.IntegerField()
    currency = models.CharField(max_length=8)
    mealInfo = models.CharField(max_length=50, null=False,  blank = True)
    status = models.CharField(max_length=20)
    shortDescription = models.CharField(max_length=8, null=False,  blank = True)
    longDescription = models.CharField(max_length=10000, null=False,  blank = True)
    externalContent = models.BooleanField()
    minimumAge = models.CharField(max_length=3, null=True, blank = True)
    wheelChairAccessible = models.BooleanField()
    featured = models.BooleanField()

