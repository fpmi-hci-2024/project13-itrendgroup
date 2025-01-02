from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm


# Create your views here.
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title':'Авторизация'}


   


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name ='users/register.html'
    extra_context = {'title':'Регистрация'}
    success_url = reverse_lazy('users:register_done')

def register_done(request):
    return render(request, 'users/register_done.html')

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title':' Профиль'}

    def get_success_url(self):
        return reverse_lazy('users:profile', args=[self.request.user.pk])

    def get_object(self, queryset=None):
        return self.request.user

class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('users:password_change_done')
    template_name = 'users/password_change_form.html'
    extra_context = {'title':' Смена пароля'}

class UserPasswordChangeDone(PasswordChangeDoneView):
    success_url = reverse_lazy('users:profile')
    template_name = 'users/password_change_done.html'


