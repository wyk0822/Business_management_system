from django.shortcuts import render, redirect, HttpResponse
import json
from userInfo.models import *

# Create your views here.

# 显示当前用户所有类别
def goods_types_views(request):
    if request.method == 'GET':
        if 'uid' in request.session:
            uid = request.session.get('uid')
            user = Administrators.objects.filter(id=uid)[0]
            goods_types = Goods_types.objects.filter(administrator_id=user.id)
            return render(request, 'B_product_type_management.html', locals())
        else:
            return redirect('/userInfo/login/')
    else:
        lid = request.POST.get('lid')
        lname = request.POST.get('lname')
        uid = request.session.get('uid')
        user = Administrators.objects.filter(id=uid)[0]

        if lid and lname:
            types = Goods_types.objects.filter(leixing=lname, leibie_id=lid)
            goods_types = []
            for i in types:
                if str(i.administrator_id) == str(user.administrator_id):
                    goods_types.append(i)

        elif lname:
            types = Goods_types.objects.filter(leixing=lname)
            goods_types = []
            for i in types:
                if str(i.administrator_id) == str(user.administrator_id):
                    goods_types.append(i)
        elif lid:
            types = Goods_types.objects.filter(leibie_id=lid)
            # print(types)
            goods_types = []
            for i in types:
                # print(type(i.administrator_id))
                # print(type(user.administrator_id))
                if str(i.administrator_id) == str(user.administrator_id):
                    goods_types.append(i)

        return render(request, 'B_product_type_management.html', locals())


# 删除类别
def del_type(request):
    lid = request.GET.get('id')
    lei = Goods_types.objects.filter(id=lid)
    if lei:
        lei.delete()
        return HttpResponse(json.dumps({'status': 1, 'msg': '删除成功'}))
    else:
        return HttpResponse(json.dumps({'status': 0, 'msg': '删除失败'}))


# 删除多个类
def del_type_two(request):
    try:
        id = request.GET.get('id')
        types = Goods_types.objects.get(id=id)
        types.delete()
        data = {'status': 1, 'msg': '删除成功'}

    except:
        data = {'status': 0, 'msg': '删除失败'}
    return HttpResponse(json.dumps(data))


# 增加类别
def add_type(request):
    try:
        if 'uid' in request.session:
            uid = request.session.get('uid')
            user = Administrators.objects.get(id=uid)
            return render(request, 'B_add_product_type.html', locals())
    except:
        return HttpResponse('加载失败,请再次刷新。。')


def add_type_1(request):
    uid = request.session.get('uid')
    user = Administrators.objects.get(id=uid)
    goods_types = Goods_types.objects.filter(administrator_id=user.id)
    lid = request.GET.get('lid', '')
    lname = request.GET.get('lname', '')
    lv = request.GET.get('lv', '')
    data = {'status': 1, 'msg': '添加成功'}
    data2 = {'status': 0, 'msg': '添加失败'}
    if lid == '' or lname == '' or lv=='':
        return HttpResponse('带\"*\"内容不允许为空。')

    elif lname != '' and lid != '' and lv != '':
        if len(goods_types) == 0:
            goods_type = Goods_types(administrator_id=user,
                                     leibie_id=lid,
                                     leixing=lname)
            goods_type.save()
            return HttpResponse(json.dumps(data))
        elif len(goods_types) != 0:
            for i in goods_types:
                if i.leibie_id == lid:
                    return HttpResponse('此类型编号已存在，请重新输入。')

                else:
                    goods_type = Goods_types(administrator_id=user,
                                            leibie_id=lid,
                                            leixing=lname,
                                            jibie=lv)
                    goods_type.save()
                    return HttpResponse(json.dumps(data))

    # elif lname != '' and lid != '' and lv == '':
    #     if len(goods_types) == 0:
    #         goods_type = Goods_types(administrator_id=user,
    #                                  leibie_id=lid,
    #                                  leixing=lname)
    #         goods_type.save()
    #         return HttpResponse(json.dumps(data))
    #     elif len(goods_types) != 0:
    #         for i in goods_types:
    #             if i.leibie_id == lid:
    #                 return HttpResponse('此类型编号已存在，请重新输入。')
    #             else:
    #                 goods_type = Goods_types(administrator_id=user,
    #                                          leibie_id=lid,
    #                                          leixing=lname)
    #                 goods_type.save()
    #                 return HttpResponse(json.dumps(data))
    #     else:
    #         return HttpResponse(json.dumps(data2))
# 修改类型
def update_type(request):
    uid = request.session.get('uid')
    user = Administrators.objects.get(id=uid)
    id = request.GET.get('id')
    goods_type = Goods_types.objects.get(id=id)
    print(id, goods_type)
    return render(request, 'B_modify_product_type.html', locals())

def update_type_1(request):
    uid = request.session.get('uid')
    user = Administrators.objects.get(id=uid)
    goods_types = Goods_types.objects.filter(administrator_id=user.id)

    id = request.GET.get('id')
    lid = request.GET.get('lid', '')
    lname = request.GET.get('lname', '')
    lv = request.GET.get('lv', '')
    goods_type = Goods_types.objects.get(id=id)

    if lid == '' or lname == '' or lv == '':
        return HttpResponse('带\"*\"内容不允许为空。')
    if lid == str(goods_type.leibie_id):
        goods_type.leixing=lname
        goods_type.jibie=lv
        print(goods_type.leibie_id, goods_type.leixing, goods_type.jibie)
        goods_type.save()

    else:
        for i in goods_types:
            if i.leibie_id == lid:
                return HttpResponse('此商品编号已存在，请重新输入。')
            else:
                goods_type.leibie_id = lid
                goods_type.leixing = lname
                goods_type.jibie = lv
                goods_type.save()

    return HttpResponse('修改成功')