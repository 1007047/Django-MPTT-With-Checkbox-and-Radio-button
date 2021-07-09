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
from .models import *
# Create your views here.


def createRadio(request):

    addressentry = get_object_or_404(Address, pk=1)



    if request.method == "POST":
        form = AddressForm(request.POST, instance=addressentry)
        if form.is_valid():

            form.save()

        else:
            print(form.errors)

    form = AddressForm(instance=addressentry)

    context = {
               'form': form,

               }
    return render(request, 'createwidget/new.html', context)

def nestedwidget(request):
    properties = Properties.objects.all()
    addressList = Address.objects.all().order_by('-id')



    checbox_input_list = list()
    i = 0
    for obj in addressList:

        temp_dict = dict()
        temp_dict[i] = json.loads(obj.checkbox_input)

        checbox_input_list.append(temp_dict)
        i += 1




    p_form = PropertyForm()



    context = {'properties': properties,
               'p_form': p_form,

               'checbox_input_list': checbox_input_list
               }
    return render(request, 'createwidget/nestedwidget.html', context)
def saveData(request):
    data = request.POST.get("data", {})
    # print ("hello",request.POST.get('form'))

    # form = Addressform2()
    # if form.is_valid():
    #     form.save()


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