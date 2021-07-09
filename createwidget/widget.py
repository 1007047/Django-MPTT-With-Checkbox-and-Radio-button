from itertools import chain

from django import forms
from django.conf import settings
from django.forms.widgets import Widget,ChoiceWidget

from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
# from django.utils.datastructures import MultiValueDict, MergeDict
# from mptt.templatetags.mptt_tags import cache_tree_children


try:
    import simplejson as json
except ImportError:
    import json


class CheckboxSelectMultiple(ChoiceWidget):
    allow_multiple_selected = True
    input_type = 'checkbox'
    #template_name = 'nestedwidget.html'
    #option_template_name = 'input_option.html'

    template_name = 'django/forms/widgets/checkbox_select.html'
    option_template_name = 'django/forms/widgets/checkbox_option.html'


    def use_required_attribute(self, initial):
        # Don't use the 'required' attribute because browser validation would
        # require all checkboxes to be checked instead of at least one.
        return False

    def value_omitted_from_data(self, data, files, name):
        # HTML checkboxes don't appear in POST data if not checked, so it's
        # never known if the value is actually omitted.
        return False

    def id_for_label(self, id_, index=None):
        """"
        Don't include for="field_0" in <label> because clicking such a label
        would toggle the first checkbox.
        """
        if index is None:
            return ''
        return super().id_for_label(id_, index)



def get_doc(node, values):
    if hasattr(node, "get_doc"):
        return node.get_doc(values)
    if hasattr(node, "name"):
        name = node.name
    else:
        name = unicode(node)
    doc = {"title": name, "key": node.pk}
    if str(node.pk) in values:
        doc['selected'] = True
        doc['expand'] = True
    return doc


