from django import forms
from django.contrib.auth.models import User


# class UserCreateForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     email = forms.EmailField()
#     first_name = forms.CharField(max_length=150)
#     last_name = forms.CharField(max_length=150)
#     password = forms.CharField(max_length=128)
#
#     def save(self):
#         username = self.cleaned_data['username']
#         firstname = self.cleaned_data['first_name']
#         lastname = self.cleaned_data['last_name']
#         email = self.cleaned_data['email']
#         password = self.cleaned_data['password']
#
#         user = User.objects.create(
#             username=username,
#             first_name=firstname,
#             last_name=lastname,
#             email=email,
#             is_staff=True,
#             is_superuser=True
#         )
#         user.set_password(password)
#
#         user.save()

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name', 'password')

    def save(self, commit=True):
        user = super().save(commit)
        user.set_password(self.cleaned_data['password'])
        user.save()

        return user



class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=128)

    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     password = self.cleaned_data.get('password')