
from rest_framework.generics import  ListAPIView

from ..models import  Store
from ..serialization.serializes import StorelistSerializer

#  一个简版的restiful 接口
class ApiStoreList(ListAPIView):
    queryset = Store.objects.all()
    serializer_class  = StorelistSerializer
    class Meta:
        model = Store
        fields = '__all__'








