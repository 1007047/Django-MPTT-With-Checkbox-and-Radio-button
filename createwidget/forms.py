from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import *
from mptt.forms import TreeNodeMultipleChoiceField, TreeNodeChoiceField
from .widget import CheckboxSelectMultiple



class PropertyForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Properties.objects.all())

    class Meta:
        model = Properties
        fields = ['name', 'parent']



class AddressForm(forms.ModelForm):

#
    class Meta:
         model = Address
         fields = ['properties_link']

         #widgets = {"properties_link": FancyTreeWidget(queryset=Properties.objects.order_by('tree_id', 'lft'),model=Properties)}
         widgets = {"properties_link": CheckboxSelectMultiple()}
