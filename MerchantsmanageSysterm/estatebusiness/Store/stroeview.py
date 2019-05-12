from django.views.generic import  ListView,UpdateView,DeleteView,DetailView

from ..models import Store
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
    success_url = 'index.html'


class StoreDetailView(DetailView):
    model = Store
    form_class = StoreDetailForm
    template_name = 'store_info.html'














2














