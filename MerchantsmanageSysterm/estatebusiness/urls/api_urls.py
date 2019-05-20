from django.conf.urls import url,include
from ..Store.apiview import ApiStoreList,ApiRentbill,StoreCitycount
app_name = 'estatebusiness'

urlpatterns = [
   url(r'storelist',ApiStoreList.as_view(),name = 'api-storelist'),
   url(r'rentbills$',ApiRentbill.as_view(),name = 'api-rentbills'),
   url(r'store/citycount$', StoreCitycount.as_view(), name='api-citycount')
]







