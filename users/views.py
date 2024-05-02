from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from users.forms import UserCreateForm, UserLoginForm


class RegisterView(View):
    def get(self, request):
        create_user = UserCreateForm()

        context = {
            'form':create_user
        }
        return render(request=request, template_name='users/register.html', context=context)

    def post(self, request):
        create_form = UserCreateForm(data=request.POST)

        if create_form.is_valid():
            create_form.save()
            return redirect('users:login')
        else:
            context = {
                'form': create_form
            }
            return render(request=request, template_name='users/register.html', context=context)

# class LoginView(View):
#     def get(self, request):
#         login_user = UserLoginForm()
#         context = {
#             'form': login_user
#         }
#         return render(request=request, template_name='users/login.html', context = context)
#
#     def post(self, request):
#         # login_form = UserLoginForm(data=request.POST)
#
#         login_form = AuthenticationForm(data=request.POST)
#
#         if login_form.is_valid():
#             # log in the user
#             print('salom dunyo')
#             return redirect('users:register')
#         else:
#             print('nima gap ozi')
#             return render(request, 'users/login.html',{'login_form': login_form})
#
#




class LoginView(View):
    def get(self, request):
        # login_form = UserLoginForm()
        login_form = AuthenticationForm()

        return render(request=request, template_name='users/login.html',context= {'form' : login_form})

    def post(self, request):
        # print(request.POST['username'], request.POST['password'])

        # login_form = UserLoginForm(data=request.POST)

        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)


            return redirect('landing_page')
        else:
            return render(request=request, template_name='users/login.html',context= {'form' : login_form})