import json

from django.shortcuts import render, redirect, HttpResponse
from userInfo.models import *
from decimal import Decimal

# Create your views here.

# 查询
def search(user):
    goods_type = Goods_types.objects.filter(administrator_id=user.id)
    goods_lst = []
    for i in goods_type:
        # print(i)
        goods = Goods.objects.filter(goods_type=i.id)
        for j in goods:
            goods_lst.append(j)
    # print(goods_lst)
    return goods_lst

# 按价格查询商品
def low_high_price(**kwargs):
    if kwargs['low_price'] != "" and kwargs['high_price'] != "":
        all_goods = Goods.objects.filter(goods_price__gte=kwargs['low_price'],
                                         goods_price__lte=kwargs['high_price'])
        goods = []
        for i in all_goods:
            if str(i.administrator_id) == str(kwargs['user'].administrator_id):
                goods.append(i)
    elif kwargs['low_price'] != "":
        goods = []
        all_goods = Goods.objects.filter(goods_price__gte=kwargs['low_price'])
        for i in all_goods:
            if str(i.administrator_id) == str(kwargs['user'].administrator_id):
                goods.append(i)
    elif kwargs['high_price'] != "":
        goods = []
        all_goods = Goods.objects.filter(goods_price__lte=kwargs['high_price'])
        for i in all_goods:
            if str(i.administrator_id) == str(kwargs['user'].administrator_id):
                goods.append(i)

    return goods





# 商品显示页面
def show_goods(request):
    if request.method == 'GET':
        if 'uid' in request.session and 'administrator_id' in request.session:
            uid = request.session.get('uid')
            user = Administrators.objects.filter(id=uid)[0]
            goods = search(user)
            return render(request, 'shangpinguanli.html', locals())
        elif 'uid' in request.COOKIES and 'administrator_id' in request.COOKIES:
            uid = request.COOKIES.get('uid')
            administrator_id = request.COOKIES.get('administrator_id')
            request.session['uid'] = uid
            request.session['administrator_id'] = administrator_id
            user = Administrators.objects.filter(id=uid)[0]
            goods = search(user)
            return render(request, 'shangpinguanli.html', locals())
        else:
            return redirect('/userInfo/login/')
    else:
        sid = request.POST.get('sid', '')
        sname = request.POST.get('sname', '')
        leibie = request.POST.get('leibie', '')
        low_price = request.POST.get('low_price', '')
        high_price = request.POST.get('high_price', '')

        uid = request.session.get('uid')
        user = Administrators.objects.get(id=uid)

        user_all_goods = search(user)


        # if sid and sname and leibie:
        #     goods = []
        #     for i in user_all_goods:
        #         if str(i.goods_id) == str(sid) and str(i.goods_name) == str(sname) and str(i.goods_type) == str(leibie):
        #             goods.append(i)


        if sid:
            goods = []
            for i in user_all_goods:
                if str(i.goods_id) == str(sid):
                    goods.append(i)


        elif sname:
            goods = []
            for i in user_all_goods:
                if str(i.goods_name) == str(sname):
                    goods.append(i)

        elif leibie:
            # lei = Goods_types.objects.filter(leixing=leibie)[0]
            goods = []
            for i in user_all_goods:
                if str(i.goods_type) == str(leibie):
                    goods.append(i)

        elif low_price:
            # goods = []
            # all_goods = Goods.objects.filter(goods_price__gte=low_price)
            # for i in all_goods:
            #     if str(i.administrator_id) == str(user.administrator_id):
            #         goods.append(i)
            goods = low_high_price(user=user, low_price=low_price, high_price=high_price)

        elif high_price:
            # goods = []
            # all_goods = Goods.objects.filter(goods_price__lte=high_price)
            # for i in all_goods:
            #     if str(i.administrator_id) == str(user.administrator_id):
            #         goods.append(i)
            goods = low_high_price(user=user, low_price=low_price, high_price=high_price)


        elif low_price and high_price:
            # all_goods = Goods.objects.filter(goods_price__gte=low_price,
            #                          goods_price__lte=high_price)
            # goods = []
            # for i in all_goods:
            #     if str(i.administrator_id) == str(user.administrator_id):
            #         goods.append(i)
            goods = low_high_price(user=user, low_price=low_price, high_price=high_price)

        return render(request, 'shangpinguanli.html', locals())
        # except:
        #     return HttpResponse('输入错误，请重新输入！！！')


# 删除商品
def del_goods(request):
    sid = request.GET.get('id')
    good = Goods.objects.filter(id=sid)
    if good:
        good.delete()
        return HttpResponse(json.dumps({'status':1, 'msg': '删除成功'}))
    else:
        return HttpResponse(json.dumps({'status':0, 'msg': '删除失败'}))


def del_goods_two(request):
    try:
        id = request.GET.get('id')
        good = Goods.objects.get(id=id)
        good.delete()
        data = {'status': 1, 'msg': '删除成功'}
    except:
        data = {'status': 0, 'msg': '删除失败'}
    return HttpResponse(json.dumps(data))



def update_goods(request):
    if 'uid' in request.session:
        uid = request.session.get('uid')
        user = Administrators.objects.get(id=uid)
        goods_types = Goods_types.objects.filter(administrator_id=user.id)
        return render(request, 'A_add_product.html', locals())

def update_goods_2(request):
    uid = request.session.get('uid')
    user = Administrators.objects.get(id=uid)
    goods = Goods.objects.filter(administrator_id=user.id)

    sid = request.GET.get('sid', '')
    goods_type_id = request.GET.get('goods_type_id', '')
    name = request.GET.get('name', '')
    kucun = request.GET.get('kucun', '')
    price = request.GET.get('price', '')
    guige = request.GET.get('guige', '')
    jifen = request.GET.get('jifen', '')
    miaoshu = request.GET.get('miaoshu', '')

    goods_type = Goods_types.objects.get(id=goods_type_id)
    print(goods_type)

    if sid=='' or goods_type_id=='' or name=='' or price=='' or kucun=='' or jifen == '':
        data = {
            'status': 1,
            'msg': '有\"*\"字段不能为空'
        }
        return HttpResponse(data.get('msg'))
    elif float(price)<0:
        return HttpResponse('价格不能低于0元')
    elif int(kucun)<0:
        return HttpResponse('库存不能低于零')
    elif float(jifen)<0:
        return HttpResponse('所需积分不能低于零')

    elif guige=='' and miaoshu=='':
        if len(goods) == 0:
            good = Goods(administrator_id=user,
                         goods_id=sid,
                         goods_name=name,
                         goods_price=price,
                        goods_type=goods_type,
                        goods_kucun=kucun,
                        goods_jifen=jifen,
                        )
            good.save()
            return HttpResponse('此商品保存成功')
        elif len(goods) != 0:
            for i in goods:
                if i.goods_id == sid:
                    return HttpResponse('此商品编号已存在，请重新输入。')

                else:
                    good = Goods(administrator_id=user,
                                 goods_id=sid,
                                 goods_name=name,
                                 goods_price=price,
                                 goods_type=goods_type,
                                 goods_kucun=kucun,
                                 goods_jifen=jifen,
                                            )
                    good.save()
                    # print(good.administrator_id, good.goods_id, good.goods_name,
                    #       good.goods_price, good.goods_type, good.goods_kucun)
                    return HttpResponse('此商品保存成功')

    elif guige=='':
        if len(goods) == 0:
            good = Goods(administrator_id=user,
                         goods_id=sid,
                         goods_name=name,
                         goods_price=price,
                         goods_type=goods_type,
                         goods_kucun=kucun,
                         goods_text=miaoshu,
                         goods_jifen=jifen,)
            # print(good.administrator_id, good.goods_id, good.goods_name,
            #       good.goods_price, good.goods_type, good.goods_kucun,good.goods_text)
            good.save()
            return HttpResponse('此商品保存成功')
        elif len(goods) != 0:
            for i in goods:
                if i.goods_id == sid:
                    return HttpResponse('此商品编号已存在，请重新输入。')

                else:
                    good = Goods(administrator_id=user,
                                 goods_id=sid,
                                 goods_name=name,
                                 goods_price=price,
                                 goods_type=goods_type,
                                 goods_kucun=kucun,
                                 goods_text=miaoshu,
                                 goods_jifen=jifen,
                                            )
                    good.save()
                    # print(good.administrator_id, good.goods_id, good.goods_name,
                    #       good.goods_pr ice, good.goods_type, good.goods_kucun, good.goods_text)
                    return HttpResponse('此商品保存成功')

    elif miaoshu=='':
        if len(goods) == 0:
            good = Goods(administrator_id=user,
                         goods_id=sid,
                         goods_name=name,
                         goods_price=price,
                         goods_type=goods_type,
                         goods_kucun=kucun,
                         goods_guige=guige,
                         goods_jifen=jifen,)
            # print(good.administrator_id, good.goods_id, good.goods_name,
            #       good.goods_price, good.goods_type, good.goods_kucun,good.goods_guige)
            good.save()
            return HttpResponse('此商品保存成功')
        elif len(goods) != 0:
            print('22222')
            for i in goods:
                if i.goods_id == sid:
                    return HttpResponse('此商品编号已存在，请重新输入。')

                else:
                    good = Goods(administrator_id=user,
                                 goods_id=sid,
                                 goods_name=name,
                                 goods_price=price,
                                 goods_type=goods_type,
                                 goods_kucun=kucun,
                                 goods_guige=guige,
                                 goods_jifen=jifen,
                                 )
                    good.save()
                    # print(good.administrator_id, good.goods_id, good.goods_name,
                    #       good.goods_price, good.goods_type, good.goods_kucun, good.goods_text)
                    return HttpResponse('此商品保存成功')


    else:
        if len(goods) == 0:
            good = Goods(administrator_id=user,
                         goods_id=sid,
                         goods_name=name,
                         goods_price=price,
                         goods_type=goods_type,
                         goods_kucun=kucun,
                         goods_guige=guige,
                         goods_text=miaoshu,
                         goods_jifen=jifen,)
            # print(good.administrator_id, good.goods_id, good.goods_name,
            #       good.goods_price, good.goods_type, good.goods_kucun,good.goods_guige)
            good.save()
            return HttpResponse('此商品保存成功')
        elif len(goods) != 0:
            print('22222')
            for i in goods:
                if i.goods_id == sid:
                    return HttpResponse('此商品编号已存在，请重新输入。')

                else:
                    good = Goods(administrator_id=user,
                                 goods_id=sid,
                                 goods_name=name,
                                 goods_price=price,
                                 goods_type=goods_type,
                                 goods_kucun=kucun,
                                 goods_guige=guige,
                                 goods_text=miaoshu,
                                 goods_jifen=jifen,
                                 )
                    good.save()
                    # print(good.administrator_id, good.goods_id, good.goods_name,
                    #       good.goods_price, good.goods_type, good.goods_kucun, good.goods_text)
                    return HttpResponse('此商品保存成功')


def change_goods(request):
    # return HttpResponse('OK')
    if 'uid' in request.session:
        uid = request.session.get('uid')
        user = Administrators.objects.get(id=uid)
        good_id = request.GET.get('good_id')
        good = Goods.objects.get(id=good_id)
        goods_types = Goods_types.objects.filter(administrator_id=user.id)
        return render(request, 'A_modify_product.html', locals())


def change_goods_2(request):
    good_id = request.GET.get('good_id')
    good = Goods.objects.get(id=good_id)
    if good:
        good.delete()
    else:
        return HttpResponse('操作失败')
    s = update_goods_2(request)
    return HttpResponse(s)





    # sid = request.GET.get('sid', '')
    # uid = request.session.get('uid')
    # user = Administrators.objects.get(id=uid)
    # goods = Goods.objects.filter(administrator_id=user.id)
    #
    # good_id = request.GET.get('good_id')

    # goods_type_id = request.GET.get('goods_type_id', '')
    # name = request.GET.get('name', '')
    # kucun = request.GET.get('kucun', '')
    # price = request.GET.get('price', '')
    # guige = request.GET.get('guige', '')
    # miaoshu = request.GET.get('miaoshu', '')
    # goods_type = Goods_types.objects.get(id=goods_type_id)
    # print(good_id, sid,  name, kucun, price, guige, miaoshu)
    #
    # if sid=='' or name=='' or price=='' or kucun=='':
    #     data = {
    #         'status': 1,
    #         'msg': '有\"*\"字段不能为空'
    #     }
    #     return HttpResponse(data.get('msg'))
    # elif float(price) < 0:
    #     return HttpResponse('价格不能低于0元')
    # elif int(kucun) < 0:
    #     return HttpResponse('库存不能低于零')
    #
    # elif guige=='' and miaoshu=='':
    #     print('@'*10)
    #     if sid == str(good.goods_id):
    #         good.goods_id = sid,
    #         good.goods_name = name,
    #         good.goods_price = price,
    #         # good.goods_type = goods_type,
    #         good.goods_kucun = kucun,
    #
    #         good.save()
    #         return HttpResponse('此商品更改成功')
    #     else:
    #         for i in goods:
    #             if i.goods_id == sid:
    #                 return HttpResponse('此商品编号已存在，请重新输入。')
    #             else:
    #                 good.goods_id = sid,
    #                 good.goods_name = name,
    #                 good.goods_price = price,
    #                 # good.goods_type = goods_type,
    #                 good.goods_kucun = kucun,
    #                 good.save()
    #                 return HttpResponse('此商品保存成功')
    # elif miaoshu != '':
    #     print('sadhhasj')
    #     return HttpResponse('112342')

    # elif guige=='':
    #     if len(goods) == 0:
    #         good = Goods(administrator_id=user,
    #                      goods_id=sid,
    #                      goods_name=name,
    #                      goods_price=price,
    #                      goods_type=goods_type,
    #                      goods_kucun=kucun,
    #                      goods_text=miaoshu)
    #         # print(good.administrator_id, good.goods_id, good.goods_name,
    #         #       good.goods_price, good.goods_type, good.goods_kucun,good.goods_text)
    #         good.save()
    #         return HttpResponse('此商品保存成功')
    #     elif len(goods) != 0:
    #         for i in goods:
    #             if i.goods_id == sid:
    #                 return HttpResponse('此商品编号已存在，请重新输入。')
    #
    #             else:
    #                 good = Goods(administrator_id=user,
    #                              goods_id=sid,
    #                              goods_name=name,
    #                              goods_price=price,
    #                              goods_type=goods_type,
    #                              goods_kucun=kucun,
    #                              goods_text=miaoshu,
    #                                         )
    #                 good.save()
    #                 # print(good.administrator_id, good.goods_id, good.goods_name,
    #                 #       good.goods_price, good.goods_type, good.goods_kucun, good.goods_text)
    #                 return HttpResponse('此商品保存成功')
    #
    # elif miaoshu=='':
    #     if len(goods) == 0:
    #         good = Goods(administrator_id=user,
    #                      goods_id=sid,
    #                      goods_name=name,
    #                      goods_price=price,
    #                      goods_type=goods_type,
    #                      goods_kucun=kucun,
    #                      goods_guige=guige)
    #         # print(good.administrator_id, good.goods_id, good.goods_name,
    #         #       good.goods_price, good.goods_type, good.goods_kucun,good.goods_guige)
    #         good.save()
    #         return HttpResponse('此商品保存成功')
    #     elif len(goods) != 0:
    #         print('22222')
    #         for i in goods:
    #             if i.goods_id == sid:
    #                 return HttpResponse('此商品编号已存在，请重新输入。')
    #
    #             else:
    #                 good = Goods(administrator_id=user,
    #                              goods_id=sid,
    #                              goods_name=name,
    #                              goods_price=price,
    #                              goods_type=goods_type,
    #                              goods_kucun=kucun,
    #                              goods_guige=guige,
    #                              )
    #                 good.save()
    #                 # print(good.administrator_id, good.goods_id, good.goods_name,
    #                 #       good.goods_price, good.goods_type, good.goods_kucun, good.goods_text)
    #                 return HttpResponse('此商品保存成功')
    #
    #
    # else:
    #     print('This is else')
    #     if len(goods) == 0:
    #         print('11111')
    #         good = Goods(administrator_id=user,
    #                      goods_id=sid,
    #                      goods_name=name,
    #                      goods_price=price,
    #                      goods_type=goods_type,
    #                      goods_kucun=kucun,
    #                      goods_guige=guige,
    #                      goods_text=miaoshu)
    #         # print(good.administrator_id, good.goods_id, good.goods_name,
    #         #       good.goods_price, good.goods_type, good.goods_kucun,good.goods_guige)
    #         good.save()
    #         return HttpResponse('此商品保存成功')
    #     elif len(goods) != 0:
    #         print('22222')
    #         for i in goods:
    #             if i.goods_id == sid:
    #                 return HttpResponse('此商品编号已存在，请重新输入。')
    #
    #             else:
    #                 good = Goods(administrator_id=user,
    #                              goods_id=sid,
    #                              goods_name=name,
    #                              goods_price=price,
    #                              goods_type=goods_type,
    #                              goods_kucun=kucun,
    #                              goods_guige=guige,
    #                              goods_text=miaoshu
    #                              )
    #                 good.save()
    #                 # print(good.administrator_id, good.goods_id, good.goods_name,
    #                 #       good.goods_price, good.goods_type, good.goods_kucun, good.goods_text)
    #                 return HttpResponse('此商品保存成功')
