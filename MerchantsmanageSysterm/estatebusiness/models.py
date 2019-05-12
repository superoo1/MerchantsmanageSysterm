from django.db import models

# Create your models here.
from django.utils.translation import ugettext_lazy as _
import uuid

class Merchant(models.Model):
    id = models.UUIDField(verbose_name = "Merchant uuid",primary_key = True,default=uuid.uuid4)
    name = models.CharField(max_length=12,blank=False,null=False,verbose_name=_("Merchant Name"))
    phone = models.CharField(max_length=12,blank=True,verbose_name=_("Merchant Phone"))
    wechat = models.CharField(max_length=12,blank=True,verbose_name=_("Merchant wechat"))




class Store(models.Model):
    id = models.IntegerField(primary_key = True,auto_created=True)
    # id = models.UUIDField(primary_key = True,default=uuid.uuid4)
    name = models.CharField(max_length=12, blank=True, verbose_name=_("Store Name"))
    address = models.CharField(max_length=12,blank=True,verbose_name=_("Store address"))
    province = models.CharField(max_length=12,blank=True,verbose_name=_("province"))
    city = models.CharField(max_length=12,blank=True,verbose_name=_("city"))
    area = models.CharField(max_length=12,blank=True,verbose_name=_("area"))



class Contract(models.Model):
    id = models.UUIDField(primary_key = True,default=uuid.uuid4)
    # 签订日期 生效日期
    sign_date = models.DateField(blank=True,verbose_name=_('sign date'))
    # 生效日期
    effect_date = models.DateField(blank=True, default='1992-08-08', verbose_name=_('effect date'))
    amount = models.CharField(blank=True,verbose_name=_('contract amount'),max_length=125)
    # 租金
    rent = models.CharField(blank=True,verbose_name=_('contract rentmoney'),max_length=125)
    comment = models.TextField(blank=True,verbose_name=_('contract comment'))
    merchant = models.ManyToManyField("estatebusiness.Merchant", related_name="Merchant", verbose_name=_('contract merchant'))
    store = models.OneToOneField("estatebusiness.Store", null = True,  verbose_name=_(' contract Store'),on_delete=models.CASCADE)


    # 经纪人
    user = models.ForeignKey('users.User',blank=True,default='', on_delete=models.CASCADE,verbose_name=_('contract agent '))

































    
















    pass
