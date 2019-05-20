from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
import uuid



class Merchant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=12,blank=False,null=False,verbose_name=_("Merchant Name"))
    phone = models.CharField(max_length=12,blank=True,verbose_name=_("Merchant Phone"))
    wechat = models.CharField(max_length=12,blank=True,verbose_name=_("Merchant wechat"))




from django.db.models import Count
from django.db import connection
class Store(models.Model):
    id = models.AutoField(primary_key=True)
    # id = models.UUIDField(primary_key = True,default=uuid.uuid4)
    name = models.CharField(max_length=12, blank=True, verbose_name=_("Store Name"))
    address = models.CharField(max_length=12,blank=True,verbose_name=_("Store address"))
    province = models.CharField(max_length=12,blank=True,verbose_name=_("province"))
    city = models.CharField(max_length=12,blank=True,verbose_name=_("city"))
    area = models.CharField(max_length=12,blank=True,verbose_name=_("area"))

    #  统计每个城市店铺数量  统计接口调用
    @classmethod
    def get_citycount(cls):
        qerys = cls.objects.values('city').annotate(num_store=Count('city'))
        print(len(qerys))
        for qery  in qerys:
            lon_lat = cls.my_custom_sql(qery['city'])
            print(lon_lat)
            qery['latitude'] = lon_lat[1]
            qery['longitude'] = lon_lat[0]
        return  qerys

    # @classmethod
    # def get_lon_lat(self,city):
    #     lon_lat =  self.objects.raw('SELECT * from s_provinces where shortName = %s and depth=2'%city)
    #     print(lon_lat)
    #
    #     pass

    from django.db import connection
    # 查询 城市所在经纬度
    @classmethod
    def my_custom_sql(cls,city):
        with connection.cursor() as cursor:
            cursor.execute("SELECT longitude,latitude from s_provinces where shortName = '%s' and depth=2"%city)
            row = cursor.fetchone()

        return row





class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    # 签订日期 生效日期
    sign_date = models.DateField(blank=True,verbose_name=_('sign date'))
    # 生效日期
    effect_date = models.DateField(blank=True, default='1992-08-08', verbose_name=_('effect date'))
    amount = models.CharField(blank=True,verbose_name=_('contract amount'),max_length=125)
    # 租金
    rent = models.CharField(blank=True,verbose_name=_('contract rentmoney'),max_length=125)
    comment = models.TextField(blank=True,verbose_name=_('contract comment'),default="")
    merchant = models.ManyToManyField("estatebusiness.Merchant", related_name="Merchant", verbose_name=_('contract merchant'))
    store = models.OneToOneField("estatebusiness.Store", null = True,related_name= "contract",  verbose_name=_(' contract Store'),on_delete=models.CASCADE)
    # 经纪人
    user = models.ForeignKey('users.User',blank=True,default='', on_delete=models.CASCADE,verbose_name=_('contract agent '))


    # 获取自身所有租金单子
    def get_rentbills(self):
        return self.rentbillls



class RentBill(models.Model):
    id = models.AutoField(primary_key = True)
    # 金额
    rent_amount = models.DecimalField(blank=True,default=0.0,max_digits=10, decimal_places=2)
    actual_date = models.DateField(blank=True,default='1992-08-08')
    real_date = models.DateField(blank=True,default='1992-08-08')
    #  到了收租日期自动提醒
    periods = models.CharField(max_length=125,blank=True,default='')
    # 外键
    contact = models.ForeignKey('estatebusiness.Contract',related_name="rentbillls",on_delete=models.CASCADE)


    # 自动化的配置  怎么搞

    # 增加一个对象 用作测试使用









































    
















    pass
