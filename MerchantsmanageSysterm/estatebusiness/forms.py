from django import forms
from .models  import *

class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = ['sign_date','rent']



class StoreUpdateForm(forms.ModelForm):

    class Meta:
        model = Store
        fields  =["name","address","city"]


        # widgets = {
        #     "name":forms.CharField()
        #
        # }

class StoreDetailForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = "__all__"











