from django.contrib import admin

from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin

# Register your models here.
admin.site.register(RadioProperties, MPTTModelAdmin)

# Register your models here.
