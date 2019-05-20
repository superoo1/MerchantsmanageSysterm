from django.views.generic import  ListView,UpdateView,DeleteView,DetailView,TemplateView

from ..models import Store,Contract
from ..forms import *
class StoreListView(ListView):
    template_name = 'store_list.html'
    # queryset = Store.objects.all()
    model = Store
    # def get_queryset(self):



class StoreUpdateView(UpdateView):
    model = Store
    form_class = StoreUpdateForm
    template_name = 'store_update.html'
    success_url = 'index'


class StoreDetailView(DetailView):
    model = Store
    # form_class = StoreDetailForm
    template_name = 'store_info.html'



    # 把跟商铺相关的合同去
    def get_contract(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        the_store= self.model.objects.get(pk=pk)
        contract = the_store.contract
        return  contract


    def get_context_data(self, **kwargs):
        contract = self.get_contract()
        contract_dic = {}
        contract_dic['contract'] = contract
        contract_dic.update(kwargs)
        return super().get_context_data(**contract_dic)



class IndexView(TemplateView):
    template_name = 'index.html'























#




#     哎
































2














