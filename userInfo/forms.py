from django import forms

from .models import *


class LoginForm(forms.ModelForm):
    class Meta:
        # 指定关联实体类
        model = Administrators
        # 指定要显示的字段
        fields = ['administrator_id', 'administrator_pwd']
        # 指定字段对应的标签
        labels = {
            'administrator_id':'账号',
            'administrator_pwd':'密 码',
        }
        # 指定字段对应的小部件
        widgets = {
            'administrator_id':forms.TextInput(
                attrs={
                    'placeholder': '请输入帐号',
                    'class': 'form-control'
                }
            ),
            'administrator_pwd': forms.PasswordInput(
                attrs={
                    'placeholder': '请输入密码',
                    'class': 'form-control'
                }
            )

        }