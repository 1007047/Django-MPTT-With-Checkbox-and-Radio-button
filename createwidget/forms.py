from django import forms
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import *
from mptt.forms import TreeNodeMultipleChoiceField, TreeNodeChoiceField


class PropertyForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=RadioProperties.objects.all())

    class Meta:
        model = RadioProperties
        fields = ['name', 'parent']


# class AddressForm(forms.ModelForm):
#     # properties_link = forms.MultipleChoiceField(
#     #     required=False, widget=forms.CheckboxSelectMultiple())
#
#     class Meta:
#         model = Address
#         fields = ['properties_link']
#
#         # widgets = {' properties_link': CheckboxInput(attrs={'class': 'required checkbox form-control'}),   }
#     class Media:
#         css = {
#             'all': 'style.css',
#         }
