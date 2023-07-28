from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from users.form import UserCreateForm, UserEditForm


# Create your views here.

class RegisterView(View):

    def get(self, request):
        create_form = UserCreateForm
        contex = {
            'form': create_form
        }
        return render(request, 'users/register.html', contex)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)
        if create_form.is_valid():
            create_form.save()
            messages.info(request, 'siz ro\'yxatdan o\'tdimgiz')
            return redirect('users:login')
        else:
            contex = {
                'form': create_form
            }
            return render(request, 'users/register.html', contex)


class LoginView(View):
    def get(self, request):
        login_form = AuthenticationForm
        contex = {
            'form': login_form
        }
        return render(request, 'users/login.html', contex)

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, "Siz tizimga kirdingiz")
            return redirect("index")
        else:
            return render(request, 'users/login.html', {"form": login_form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Siz tizimdan chiqtingiz")
        return redirect("index")


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        return render(request, "users/profile.html", {"user": user})


class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request):
        edit_form = UserEditForm(instance=request.user)
        contex = {
            'form': edit_form
        }
        return render(request, 'users/profile_edit.html', contex)

    def post(self, request):
        edit_form = UserEditForm(
            instance=request.user,
            data=request.POST,
            files=request.FILES
        )
        if edit_form.is_valid():
            edit_form.save()
            messages.info(request, "Ma'lumotlar muofiqaiyatli yangilandi")
            return redirect('users:profile')

        return render(request, "users/profile_edit.html", {"form": edit_form})