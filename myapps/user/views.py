import json

from django.shortcuts import render, redirect


# Create your views here.
from user.forms import UserForm


def regist(request):
    if request.method == 'POST':
        # 读取 request.POST字典中的数据，借助UserProfile模型保存到数据库
        # 通过ModelForm模型表单类 验证数据并保存到数据库中
        userForm = UserForm(request.POST)
        if userForm.is_valid(): # 判断必须要字段是否都存在数据
            userForm.save()  # 保存数据
            return redirect('/')

        # post提交时有验证错误，将验证错误转成json－> dict对象
        errors = json.loads(userForm.errors.as_json())
        print(errors)

    return render(request, 'user/regist.html', locals())