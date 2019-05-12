from django.conf.urls  import url,include
from ..import views
from ..Store import stroeview
app_name = 'estatebusiness'

urlpatterns = [
    url(r'^contract/create',views.ContractCreateview.as_view(),name='contractCreate'),
   url(r'^storelist',stroeview.StoreListView.as_view(),name='storelist'),
    url(r'^store/(?P<pk>[0-9a-zA-Z\-]{1,36})/update/$', stroeview.StoreUpdateView.as_view(), name='store-update'),
    url(r'^store/(?P<pk>[0-9a-zA-Z\-]{1,36})/detail/$', stroeview.StoreDetailView.as_view(), name='store-detail')

]


