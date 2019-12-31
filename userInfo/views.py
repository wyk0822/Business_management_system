import json, sys
from django.shortcuts import render, redirect, HttpResponse
from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
import re, random
from userInfo import utils
from userInfo.forms import LoginForm
from .models import *
from hashlib import sha1


# 登录
def login_view(request):
    if request.method == 'GET':
        # 获取请求原地址，如果没有的话取‘/’
        # url = request.META.get('HTTP_REFERER', '/')
        # 判断session中是否有uid和uphone
        if 'uid' in request.session and 'administrator_id' in request.session:
            return redirect('/')
        else:
            if 'uid' in request.COOKIES and 'administrator_id' in request.COOKIES:
                uid = request.COOKIES.get('uid')
                administrator_id = request.COOKIES.get('administrator_id')
                request.session['id'] = uid
                request.session['administrator_id'] = administrator_id
                return redirect('/')
            else:
                # 构造相应对象，并将url保存进cookies,供post使用
                captcha = utils.captcha()
                resp = render(request, 'login.html', locals())
                return resp
    else:
        # try:
        captchaStr = request.POST.get('security_code')
        if captchaStr:
            captchaHashkey = request.POST.get('hashkey')
            # print(captchaStr, ":", captchaHashkey)
            # 验证结果
            verification_results = utils.jarge_captcha(captchaStr, captchaHashkey)
            # print('verification_results', verification_results)

            if verification_results:
                administrator_id = request.POST.get('administrator_id')
                # 判断administrator_id中是否含有字母，含有则返回id不符合规范
                if re.findall('\D', administrator_id):
                    return HttpResponse("账号不符合规范")
                if administrator_id == "":
                    return HttpResponse("账号不能为空")

                administrator_pwd = request.POST.get('administrator_pwd')
                s1 = sha1()
                # 对s1进行更新
                s1.update(administrator_pwd.encode())
                # 加密处理
                administrator_pwd = s1.hexdigest()
                # print(administrator_pwd)
                user = Administrators.objects.filter(administrator_id=administrator_id,
                                                     administrator_pwd=administrator_pwd)
                if user:
                    # 登录成功， 将uid和uphon保存进session
                    id = user[0].id
                    request.session['uid'] = id
                    request.session['administrator_id'] = administrator_id

                    resp = redirect('/')
                    # 如果curl存在于cookies中，则将curl从cookies中删除
                    if 'isSave' in request.POST:
                        resp.set_cookie('uid', id, 60 * 60 * 24 * 365)
                        resp.set_cookie('administrator_id', administrator_id, 60 * 60 * 24 * 365)
                    return resp
                else:
                    # 登录失败，回到登录页面
                    dic = {
                        'status_code': 0,
                        'msg': '账号或密码不正确！！！'
                    }
                    return HttpResponse(json.dumps(dic))
                # except:
                #     return HttpResponse('输入账号或密码有误')
            else:
                return HttpResponse('验证码输入错误')
        else:
            return HttpResponse('验证码不能为空！！！')

        # administrator_id = request.POST.get('administrator_id')
        # # 判断administrator_id中是否含有字母，含有则返回id不符合规范
        # if re.findall('\D', administrator_id):
        #     return HttpResponse("账号不符合规范")
        # if administrator_id == "":
        #     return HttpResponse("账号不能为空")
        #
        # administrator_pwd = request.POST.get('administrator_pwd')
        # s1 = sha1()
        # # 对s1进行更新
        # s1.update(administrator_pwd.encode())
        # # 加密处理
        # administrator_pwd = s1.hexdigest()
        # # print(administrator_pwd)
        # user = Administrators.objects.filter(administrator_id=administrator_id,
        #                                      administrator_pwd=administrator_pwd)
        # if user:
        #     # 登录成功， 将uid和uphon保存进session
        #     id = user[0].id
        #     request.session['uid'] = id
        #     request.session['administrator_id'] = administrator_id
        #
        #     resp = redirect('/')
        #     # 如果curl存在于cookies中，则将curl从cookies中删除
        #     if 'isSave' in request.POST:
        #         resp.set_cookie('uid', id, 60 * 60 * 24 * 365)
        #         resp.set_cookie('administrator_id', administrator_id, 60 * 60 * 24 * 365)
        #     return resp
        # else:
        #     # 登录失败，回到登录页面
        #     dic = {
        #         'status_code': 0,
        #         'msg': '账号或密码不正确！！！'
        #     }
        #     return HttpResponse(json.dumps(dic))
        # # except:
        # #     return HttpResponse('输入账号或密码有误')


# 注册
def register_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        administrator_id = request.POST.get('administrator_id')
        if re.findall('\D', administrator_id):
            return HttpResponse("账号不符合规范")

        administrator_name = request.POST.get('administrator_name')
        administrator_pwd = request.POST.get('administrator_pwd')
        administrator_pwd2 = request.POST.get('administrator_pwd2')
        if administrator_pwd == administrator_pwd2:
            s1 = sha1()
            # 对s1进行更新
            s1.update(administrator_pwd.encode())
            # 加密处理
            administrator_pwd = s1.hexdigest()
            print(administrator_pwd)

            user = Administrators(administrator_id=administrator_id,
                                  administrator_name=administrator_name,
                                  administrator_pwd=administrator_pwd)
            user.save()
            return redirect('/userInfo/login')
        else:
            return HttpResponse("密码两次输入不一致")


# 退出账号
def logout_views(request):
    if 'uid' in request.session and 'administrator_id' in request.session:
        del request.session['uid']
        del request.session['administrator_id']
        # 获取原地址，构建响应对象
        # url = request.META.get('HTTP_REFERER', '/')
        resp = redirect('/userInfo/login/')
        # 判断cookie有则清除
        if 'uid' in request.COOKIES and 'administrator_id' in request.COOKIES:
            resp.delete_cookie('uid')
            resp.delete_cookie('administrator_id')
        return resp
    return redirect('/userInfo/login/')


# 注册是判断账号是否存在
def check_uphone_views(request):
    uphone = request.GET.get('administrator_id')
    users = Administrators.objects.filter(administrator_id=uphone)
    if users:
        dic = {
            'status': 1,
            'msg': '帐号已存在',
        }
    else:
        dic = {
            'status': 0,
            'msg': '通过',
        }
    return HttpResponse(json.dumps(dic))


def settings(request):
    if 'uid' in request.session:
        uid = request.session.get('uid')
        user = Administrators.objects.get(id=uid)
        return render(request, 'user_msg.html', locals())


def settings_2(request):
    if 'uid' in request.session:
        try:
            uid = request.session.get('uid')
            user = Administrators.objects.get(id=uid)
            name = request.GET.get('name')
            jifen = request.GET.get('jifen')
            user.administrator_name = name
            user.administrator_jifen = float(jifen)
            user.save()
            return HttpResponse('保存成功')
        except:
            return HttpResponse('保存失败')

# 修改密码
def update_pwd(request):
    if 'uid' in request.session:
        # try:
        uid = request.session.get('uid')
        user = Administrators.objects.get(id=uid)
        pwd = request.GET.get('new_pwd', "")
        pwd_2 = request.GET.get("new_pwd_2", "")
        old_pwd = request.GET.get('old_pwd', "")
        if jiami(old_pwd) != user.administrator_pwd:
            return HttpResponse('旧密码输入错误！！！')
        if pwd != pwd_2:
            return HttpResponse('两次密码不一致，请重新输入！！！')
        elif pwd == "" or pwd_2 == "":
            return HttpResponse('密码不能为空')
        elif pwd == pwd_2:
            user.administrator_pwd = jiami(pwd)
            user.save()
            return HttpResponse('密码修改成功')
        # except:
        #     return HttpResponse('密码修改失败')

def forget_pwd(request):
    return render(request, 'email_modfiy_pwd.html', locals())

# 导入自定义发送邮件模块
sys.path.append("../../")
from lib import send_email_demo
#邮件修改密码
def email_modfiy_pwd(request):
    useremail_id = request.GET.get("useremail_id")
    print(useremail_id)
    # user_id = '18733181565@163.com'  # 收件人邮箱账号
    send_email_code = ""
    for i in range(6):
        msg = str(random.randint(0, 9))
        print(msg)
        send_email_code+=msg
    print(send_email_code)
    send_email_demo.mail(useremail_id, send_email_code)
    return HttpResponse(json.dumps({"status":1, "msg": "send successful"}))

def jiami(req_Pwd):
    s1 = sha1()
    # 对s1进行更新
    s1.update(req_Pwd.encode())
    # 加密处理
    administrator_pwd = s1.hexdigest()
    return administrator_pwd


def security_code(request):
    captcha = utils.captcha()
    if request.method == "POST":
        # 获取验证码
        captchaStr = request.POST.get('code')
        captchaHashkey = request.POST.get('hashkey')
        print(captchaStr, ":", captchaHashkey)
        aaa = utils.jarge_captcha(captchaStr, captchaHashkey)
        print('aaa', aaa)
        if aaa:
            return render(request, 'home.html')
        return render(request, 'login.html', context=locals())
    return render(request, 'login.html', context=locals())


def update_security_img(request):
    captcha = utils.captcha()
    print('update_security_img:', captcha)
    return HttpResponse(json.dumps(captcha))



def test_html(request):

    return render(request, 'test.html')

