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
import json
# Create your views here.


def createRadio(request):
    properties = RadioProperties.objects.all()
    addressList = Address.objects.all()
    # print ("addressList",addressList)

    checbox_input_list = []

    if len(addressList) > 0:
        obj = Address.objects.last()
        checbox_input_list = json.loads(obj.checkbox_input)


    # print ("checbox_input_list",checbox_input_list)

    # All insert When Radio entry empty
    if len(properties) == 0:
        obj = RadioProperties()
        obj.name = "Root"
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
        # form = AddressForm()




    context = {'properties': properties,
               'p_form': p_form,
               # 'form': form
               'checbox_input_list': checbox_input_list
               }
    return render(request, 'createwidget/index.html', context)


def saveData(request):
    data = request.POST.get("data", {})
    # print("json is ",data)


    obj = Address()
    obj.checkbox_input = data
    # addresslist = Address.objects.all()

    # if len(addresslist) == 0:
    #     # obj = Address()
    #     # obj.id = 1
    #     # obj.checkbox_input = data
    #
    # else:
    #
    #     # obj = Address.objects.last
    #     # obj.id = 1
    #     # obj.checkbox_input = data


    try:
        obj.save()

    except Exception as e:
        print("e "+str(e))
        return HttpResponse(status=500)

    return HttpResponse(status=200)