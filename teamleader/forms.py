from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import choose ,Cfmerchant

class chooseform(ModelForm):
    class Meta:
        model = choose
        db_table = 'teamleader_choose'
        managed = True
        fields = ['loanofficer_name','employee']
