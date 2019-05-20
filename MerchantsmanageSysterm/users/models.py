from django.db import models

# Create your models here.
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
import uuid
from django import forms

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    name =  models.CharField(max_length=12,verbose_name =_('User name'),blank=True,default="")
    groups = models.ManyToManyField('UserGroup', related_name='users',blank=True,  default="", verbose_name=_('User group'))
    role = models.ManyToManyField('UserRole', related_name='role',default="1",verbose_name = "roles")
    wechat = models.CharField( max_length=128, blank=True, verbose_name=_('Wechat'),default="")
    phone = models.CharField( max_length=20, blank=True, null=True, verbose_name=_('Phone'),default="")
    # name = models.CharField( max_length=20,blank=True,verbose_name=_('User name'))


    # USERNAME_FIELD = "name"



class UserGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, verbose_name="GroupName")
    comment = models.TextField(blank=True, verbose_name=_('Comment'))
    date_created = models.DateTimeField(auto_now_add=True, null=True,verbose_name=_('Date created'))



class UserRole(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=120, verbose_name="RoleName")
    # Rolepermission = models.CharField("RolePersmission",default='11',verbose_name=_('Rolepermission'))
    date_created = models.DateTimeField(auto_now_add=True, null=True, verbose_name=_('Date created'))





from django.contrib.auth.hashers import make_password

class UserForm(forms.ModelForm):
    # your_name = forms.CharField(label='Your name', max_length=100)
    class Meta:
        model = User
        fields = ['username','password']

    def clean_password(self):
        password = self.cleaned_data['password']
        password_sec = make_password(password)
        return password_sec



from django.contrib.auth.forms import AuthenticationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label=_('Username'), max_length=100)
    password = forms.CharField(
        label=_('Password'), widget=forms.PasswordInput,
        max_length=128, strip=False
    )





















