from django.shortcuts import render
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.views.generic import CreateView
from users.forms import UserForm
from users.models import User

class LoginView(BaseLoginView):
   template_name = 'users/login.html'

class LogoutView(BaseLogoutView):
   pass

class RegisterView(CreateView):
   model = User
   form_class = UserForm
   template_name = 'users/users_register.html'
   success_url = '/users/login/'