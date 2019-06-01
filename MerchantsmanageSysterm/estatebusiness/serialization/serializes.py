
from rest_framework import  serializers
from .. models import  *

class StorelistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'




class RentbillSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentBill
        fields = "__all__"




#  没有用modelSerializer
class StoreCitycountSerializer(serializers.Serializer):

    # num_store =   serializers.SerializerMethodField()
    num_store = serializers.IntegerField(read_only=True)
    city= serializers.CharField(required=False, allow_blank=True, max_length=100)
    longitude = serializers.CharField(required=False, allow_blank=True, max_length=16)
    latitude = serializers.CharField(required=False, allow_blank=True, max_length=16)


