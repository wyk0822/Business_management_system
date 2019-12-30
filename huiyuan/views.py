import json

from django.shortcuts import render, redirect, HttpResponse
from userInfo.models import *
# Create your views here.

def show_huiyuan(request):
    if 'uid' in request.session:
        uid = request.session.get('uid')
        user = Administrators.objects.filter(id=uid)[0]
        buy_peoples = Buy_peoples.objects.filter(administrator_id=user.id).order_by('-id')
        index = 0

        peoples = []
        peoples_after = []

        for i in buy_peoples:
            peoples.append(i)
        for i in peoples:
            if i.buy_people_is_show == 0 or i.buy_people_is_show=='false':
                pass
            else:
                peoples_after.append(i)
            index+=1
        return render(request, 'D_member_management.html', locals())
    else:
        return redirect('/userInfo/login/')

# 添加会员
def add_huiyuan(request):
    if 'uid' in request.session:
        uid = request.session.get('uid')
        user = Administrators.objects.filter(id=uid)[0]
        return render(request, 'D_add_member.html', locals())
    else:
        return redirect('/userInfo/login/')


def add_huiyuan_2(request):
    uid = request.session.get('uid')
    user = Administrators.objects.get(id=uid)

    name = request.GET.get('name', '')
    sex = request.GET.get('sex', '')
    phone = request.GET.get('phone', '')
    age = request.GET.get('age', '')
    addr = request.GET.get('addr', '')
    all_huiyuan = Buy_peoples.objects.filter(administrator_id=user.id)

    for i in all_huiyuan:
        if i.buy_people_name==name and i.buy_people_phone==phone:
            return HttpResponse('此用户已存在')
        # elif i.buy_people_name==name and i.buy_people_phone==phone and i.buy_people_is_show==0:
        #
        #     return HttpResponse('用户添加成功')

    if len(phone)<11:
        return HttpResponse('手机号不符合格式，请正确输入')


    # print(name, sex, phone, age, addr)

    if name == '' or sex == '' or phone=='' or age=='':
        return HttpResponse('带\"*\"内容不允许为空。')

    elif name and sex and phone and age and addr == '':
        # print('111111111111')
        people = Buy_peoples(administrator_id=user,
                             buy_people_name=name,
                             buy_people_phone=phone,
                             buy_people_age=age,
                             buy_people_sex=sex,)
        # print(people)
        people.save()
        return HttpResponse('此会员添加成功')

    elif name and sex and phone and age and addr:
        # print('22222222222')
        people = Buy_peoples(administrator_id=user,
                             buy_people_name=name,
                             buy_people_phone=phone,
                             buy_people_age=age,
                             buy_people_sex=sex,
                             buy_people_addr=addr)
        # print(people)
        people.save()
        return HttpResponse('此会员添加成功')
    else:
        return HttpResponse('输入有误请重新输入')


# 删除会员
def del_huiyuan(request):
    huiyuan_id = request.GET.get('id', '')
    # print(huiyuan_id)
    huiyuan = Buy_peoples.objects.get(id=huiyuan_id)
    if huiyuan:
        huiyuan.buy_people_is_show = 0
        huiyuan.save()
        return HttpResponse(json.dumps({'status': 1, 'msg': '删除成功'}))
    else:
        return HttpResponse(json.dumps({'status': 0, 'msg': '删除失败'}))


# 删除多个会员
def del_huiyuan_s(request):
    data = {'status': 1, 'msg': '删除成功'}
    data2 = {'status': 0, 'msg': '删除失败'}
    try:
        id = request.GET.get('id')
        huiyuans = Buy_peoples.objects.get(id=id)
        if huiyuans:
            huiyuans.buy_people_is_show = 0
            huiyuans.save()
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponse(json.dumps(data2))
    except:
        return HttpResponse(json.dumps(data2))

# 修改会员信息
def change_huiyuan(request):
    # return HttpResponse('OK')
    if 'uid' in request.session:
        uid = request.session.get('uid')
        user = Administrators.objects.get(id=uid)
        huiyuan_id = request.GET.get('id')
        people = Buy_peoples.objects.get(id=huiyuan_id)
        return render(request, 'D_modify_member.html', locals())


def change_huiyuan_2(request):
    huiyuan_id = request.GET.get('id')
    print(huiyuan_id)
    people = Buy_peoples.objects.get(id=huiyuan_id)
    print(people)
    if people:
        people.delete()
    else:
        return HttpResponse('操作失败')
    s = add_huiyuan_2(request)
    return HttpResponse(s)


# 查询
def select_huiyuan(request):
    uid = request.session.get('uid')
    user = Administrators.objects.get(id=uid)

    name = request.GET.get('name', '')
    sex = request.GET.get('sex', '')

    phone = request.GET.get('phone', '')
    age = request.GET.get('age', '')
    print('age', age)
    if sex == '男':
        sex = 'a'
    elif sex == '女':
        sex = 'b'

    if name and sex and phone and age:
        peoples_query_set = Buy_peoples.objects.filter(buy_people_name=name, buy_people_phone=phone,
                                           buy_people_age=age, buy_people_sex=sex)
        peoples_after = []
        for i in peoples_query_set:
            if str(i.administrator_id) == str(user.administrator_id)and i.buy_people_is_show==1:
                peoples_after.append(i)

    elif name and sex and phone:
        peoples_query_set = Buy_peoples.objects.filter(buy_people_name=name, buy_people_phone=phone,
                                                       buy_people_sex=sex)
        peoples_after = []
        for i in peoples_query_set:
            if str(i.administrator_id) == str(user.administrator_id) and i.buy_people_is_show == 1:
                peoples_after.append(i)
    elif name and sex and age:
        peoples_query_set = Buy_peoples.objects.filter(buy_people_name=name,
                                                       buy_people_age=age, buy_people_sex=sex)
        peoples_after = []
        for i in peoples_query_set:
            if str(i.administrator_id) == str(user.administrator_id) and i.buy_people_is_show == 1:
                peoples_after.append(i)
    elif name and age and phone:
        peoples_query_set = Buy_peoples.objects.filter(buy_people_name=name, buy_people_phone=phone,
                                                       buy_people_age=age)
        peoples_after = []
        for i in peoples_query_set:
            if str(i.administrator_id) == str(user.administrator_id) and i.buy_people_is_show == 1:
                peoples_after.append(i)
    elif phone and sex and age:
        peoples_query_set = Buy_peoples.objects.filter(buy_people_phone=phone,
                                                       buy_people_age=age, buy_people_sex=sex)
        peoples_after = []
        for i in peoples_query_set:
            if str(i.administrator_id) == str(user.administrator_id) and i.buy_people_is_show == 1:
                peoples_after.append(i)

    elif phone and age:
        peoples_query_set = Buy_peoples.objects.filter(buy_people_phone=phone,
                                                       buy_people_age=age)
        peoples_after = []
        for i in peoples_query_set:
            if str(i.administrator_id) == str(user.administrator_id) and i.buy_people_is_show == 1:
                peoples_after.append(i)
    elif name and sex:
        peoples_query_set = Buy_peoples.objects.filter(buy_people_name=name,
                                                       buy_people_sex=sex)
        peoples_after = []
        for i in peoples_query_set:
            if str(i.administrator_id) == str(user.administrator_id) and i.buy_people_is_show == 1:
                peoples_after.append(i)
    elif name and age:
        peoples_query_set = Buy_peoples.objects.filter(buy_people_name=name,
                                                       buy_people_age=age)
        peoples_after = []
        for i in peoples_query_set:
            if str(i.administrator_id) == str(user.administrator_id) and i.buy_people_is_show == 1:
                peoples_after.append(i)
    elif name and phone:
        peoples_query_set = Buy_peoples.objects.filter(buy_people_name=name, buy_people_phone=phone)
        peoples_after = []
        for i in peoples_query_set:
            if str(i.administrator_id) == str(user.administrator_id) and i.buy_people_is_show == 1:
                peoples_after.append(i)
    elif sex and phone:
        peoples_query_set = Buy_peoples.objects.filter(buy_people_phone=phone,
                                                       buy_people_sex=sex)
        peoples_after = []
        for i in peoples_query_set:
            if str(i.administrator_id) == str(user.administrator_id) and i.buy_people_is_show == 1:
                peoples_after.append(i)
    elif sex and age:
        peoples_query_set = Buy_peoples.objects.filter(buy_people_age=age, buy_people_sex=sex)
        peoples_after = []
        for i in peoples_query_set:
            if str(i.administrator_id) == str(user.administrator_id) and i.buy_people_is_show == 1:
                peoples_after.append(i)

    elif name:
        peoples_query_set = Buy_peoples.objects.filter(buy_people_name=name)
        peoples_after = []
        for i in peoples_query_set:
            if str(i.administrator_id) == str(user.administrator_id) and i.buy_people_is_show==1:
                peoples_after.append(i)

    elif sex:
        peoples_query_set = Buy_peoples.objects.filter(buy_people_sex=sex)
        peoples_after = []
        for i in peoples_query_set:
            if str(i.administrator_id) == str(user.administrator_id)and i.buy_people_is_show==1:
                peoples_after.append(i)
    elif phone:
        peoples_query_set = Buy_peoples.objects.filter(buy_people_phone=phone)
        peoples_after = []
        for i in peoples_query_set:
            if str(i.administrator_id) == str(user.administrator_id)and i.buy_people_is_show==1:
                peoples_after.append(i)
    elif age:
        peoples_query_set = Buy_peoples.objects.filter(buy_people_age=age)
        peoples_after = []
        for i in peoples_query_set:
            if str(i.administrator_id) == str(user.administrator_id)and i.buy_people_is_show==1:
                peoples_after.append(i)

    return render(request, 'D_member_management.html', locals())