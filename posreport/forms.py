#coding=utf-8
from django import  forms
from django.conf import settings
from django.contrib.auth.models import User
#登陆表单
class login_form(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"placeholder":u"请输入用户名","required":"required","class":"form-control"}), max_length=50,error_messages={"required":u"username不能为空",},label='用户')
    password=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":u"请输入密码","required":"required","class":"form-control"}),max_length=20,error_messages={"required":u"密码不能为空"},label="密码")