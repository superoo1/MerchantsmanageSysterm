
from django.conf.urls import url,include
from .. import views

app_name = "users"

urlpatterns = [
    url(r'^register',views.UserRrgister.as_view(),name="register"),
    url(r'^login', views.UserLogin.as_view(), name="login")
]

