from django.db import models

# Create your models here.
# Create your models here.
from django.contrib.auth.models import AbstractUser

import uuid


class User(AbstractUser):
    id = models.UUIDField(verbose_name = "uuid",primary_key = True,default=uuid.uuid4)
    username =  models.CharField(max_length=12,verbose_name ="usrname")
    groups = models.ManyToManyField('UserGroup', related_name='users',blank=True, verbose_name=_('User group'))
    role = models.ManyToManyField('UserRole', related_name='role',default="1",verbose_name = "roles")
    wechat = models.CharField( max_length=128, blank=True, verbose_name=_('Wechat'))
    phone = models.CharField( max_length=20, blank=True, null=True, verbose_name=_('Phone'))



class UserGroup(models.Model):
    id = models.UUIDField(verbose_name="uuid", primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=120, verbose_name="GroupName")
    comment = models.TextField(blank=True, verbose_name=_('Comment'))
    date_created = models.DateTimeField(auto_now_add=True, null=True,verbose_name=_('Date created'))



class UserRole(models.Model):
    id = models.UUIDField(verbose_name="uuid", primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=120, verbose_name="RoleName")
    permission = models.CharField("RolePersmission",default='11',verbose_name="RolePersmission")
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_('Date created'))


















