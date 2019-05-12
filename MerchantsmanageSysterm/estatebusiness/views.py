from django.shortcuts import render
from .models import *
from .forms  import *
# Create your views here.
from django.views.generic import CreateView

class ContractCreateview(CreateView):
    model = Contract
    form_class = ContractForm
    success_url = 'index.html'
    template_name = 'contract_create.html'
    def form_valid(self, form):
        print(form.fields)
        return super().form_valid(form)

















