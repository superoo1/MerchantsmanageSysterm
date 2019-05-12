from django.conf.urls import url,include
from ..Store.apiview import ApiStoreList
app_name = 'estatebusiness'

urlpatterns = [
   url(r'storelist',ApiStoreList.as_view(),name = 'api-storelist')
]

