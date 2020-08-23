from django.shortcuts import render
from django.http import HttpResponse
from .form import LoginForm
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    login_form = LoginForm()
    return render(request, 'form2.html', {'form': login_form, 'message': ''})


def login2(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # 读取表单的返回值
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                # 登陆用户
                login(request, user)
                return HttpResponse('登录成功')
            else:
                return render(request, 'form2.html', {'form': login_form, 'message': '用户或密码错误'})
