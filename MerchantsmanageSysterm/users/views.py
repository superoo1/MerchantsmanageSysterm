from django.shortcuts import render

# Create your views here.
import django.contrib.auth.context_processors
from django.views.generic.edit import FormView ,CreateView
class UserLogin():
    pass


from  .models import User,UserForm,UserLoginForm
from django.shortcuts import reverse, redirect

class UserRrgister(CreateView):
    model = User
    form_class =UserForm
    template_name = 'users/user_register.html'
    success_url ='/business/storelist'

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['form'] = self.get_form()
            print(kwargs)
        print(kwargs['form'])
        print(kwargs['form'].errors.as_data())
        print(kwargs['form'].data)
        return super().get_context_data(**kwargs)

class UserLogin(FormView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    success_url = '/business/storelist'

    # 终于能够登陆了
    def form_valid(self, form):
        # ip = get_login_ip(self.request)
        print(form.fields)
        return super().form_valid(form)





















