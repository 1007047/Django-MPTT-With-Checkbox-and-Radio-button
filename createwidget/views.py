from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, Http404, HttpResponseNotAllowed
from .forms import *
from .models import *

# Create your views here.


def createRadio(request):
    properties = RadioProperties.objects.all()

    # All insert When Radio entry empty
    if len(properties) == 0:
        obj = RadioProperties()
        obj.name = "All"
        obj.save()



    if request.method == 'POST':
        p_form = PropertyForm(request.POST)
        # form = AddressForm(request.POST)
        # if p_form.is_valid() and form.is_valid():
        if p_form.is_valid():
            p_form.save()
            # form.save()
            # message.success(
            #     request, 'post created successfully!')
            return redirect('createradio')
    else:
        p_form = PropertyForm()




    context = {'properties': properties,
               'p_form': p_form,
               # 'form': form
               }
    return render(request, 'createwidget/index.html', context)