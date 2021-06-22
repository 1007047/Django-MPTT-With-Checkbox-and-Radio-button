from django.db import models
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.signals import post_save
# Create your models here.



class RadioProperties(MPTTModel):
    name = models.CharField(max_length=32)
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']
