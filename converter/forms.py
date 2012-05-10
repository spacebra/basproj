from django import forms
from django.db import connection

from converter.models import Student

class DropDownList(forms.Form):
    tables = connection.introspection.table_names()
    seen_models = connection.introspection.installed_models(tables)

    choice = []
    for model in seen_models:
        if "converter" in str(model):
            choice.append((model.__name__,model.__name__))

    #list = forms.ModelChoiceField(queryset=seen_models, widget=forms.RadioSelect, empty_label=None)
    # list = forms.ChoiceField(widget=forms.RadioSelect, choices = ([('1','1'), ('2','2'),('3','3'), ]) )
    list = forms.ChoiceField(widget=forms.RadioSelect, choices=choice )