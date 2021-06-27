from django.db import models
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.signals import post_save
# Create your models here.
# import logging
# from django.views.generic.detail import *
from django.views.generic.detail import BaseDetailView

class RadioProperties(MPTTModel):
    name = models.CharField(max_length=32)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Address(models.Model):
    id = models.AutoField(primary_key=True)
    # properties_link = models.ManyToManyField(RadioProperties, blank=True, default=None )
    checkbox_input = models.CharField(max_length=5000, null=False, blank=False)



# class Address2(LoggerModelMixin,Standard_Model_Mixin):
class Address2(models.Model):
    properties_link = models.ManyToManyField(RadioProperties, default=None )