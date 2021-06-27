from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.createRadio, name='createradio'),
    path('nestedwidget', views.nestedwidget, name='nestedwidget'),
    path('datasave', views.saveData, name="datasave"),
]
