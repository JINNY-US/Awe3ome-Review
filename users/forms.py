from .models import Users
from django.contrib.auth.forms import UserChangeForm  # user프로필 수정
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput, Textarea

class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'email', 'password', 'bio']

        widgets = {
            'username': TextInput(attrs={
                'class': "form-control",  # 부트스트랩 적용에 필요!
                'placeholder': 'ID'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email'
            }),
            'password': PasswordInput(attrs={
                'class': "form-control",
                'style': "font-family: sans-serif",
                'placeholder': 'Password'
            }),
            'bio': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'bio'
            }),
        }


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = Users
        fields = ['email', 'bio']

        widgets = {
            'email': EmailInput(attrs={
                'class': "form-control",
                'placeholder': 'Email'
            }),
            'bio': Textarea(attrs={
                'class': "form-control",
                'placeholder': 'comment'
            }),
        }
