
from rest_framework.generics import  ListAPIView

from ..models import  *
from ..serialization.serializes import *

#  一个简版的restiful 接口
class ApiStoreList(ListAPIView):
    queryset = Store.objects.all()
    serializer_class  = StorelistSerializer
    class Meta:
        model = Store
        fields = '__all__'




#  获取 合同所有租金账单的一个接口
# 错了 不应该写成这样的接口
class ApiRentbill(ListAPIView):
    serializer_class = RentbillSerializer
    def get_contract(self):
        pk = self.kwargs.get(self.lookup_field)
        contract = Contract.objects.get(pk=1)
        return  contract


    def get_queryset(self):
        contract = self.get_contract()
        queryset = contract.get_rentbills()
        return queryset

    class Meta:
        model = RentBill
        fields = "__all__"



class StoreCitycount(ListAPIView):
    serializer_class = StoreCitycountSerializer



    def get_queryset(self):
        return Store.get_citycount()



















































