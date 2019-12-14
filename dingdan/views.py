from django.shortcuts import render, HttpResponse, redirect
import json
from datetime import datetime
from decimal import Decimal
from userInfo.models import *

# Create your views here.
# 显示订单信息
DIC = {'goods':'',
       'people':''}


def show_order(request):
    if 'uid' in request.session:
        uid = request.session.get('uid')
        user = Administrators.objects.filter(id=uid)[0]
        orders_top = Order.objects.filter(administrator_id=user.id).order_by('-id')

        orders = []
        for i in orders_top:
            # goods = i.goods.all()
            # print(goods)
            print(i.dingdanshijian.strftime('%Y-%m-%d %H:%M:%S'))
            if i.order_is_show == 1:
                orders.append(i)
        return render(request, 'C_订单管理.html', locals())


# 选择用户
def select_peoples(request):
    if 'uid' in request.session and 'administrator_id' in request.session:
        uid = request.session.get('uid')
        user = Administrators.objects.filter(id=uid)[0]
        peoples = Buy_peoples.objects.filter(administrator_id=user.id)

        peoples_after = []

        for i in peoples:
            if i.buy_people_is_show == 0 or i.buy_people_is_show == 'false':
                pass
            else:
                peoples_after.append(i)
        return render(request, 'C_选择会员.html', locals())


# 选择用户
def select_goods(request):
    if 'uid' in request.session and 'administrator_id' in request.session:
        uid = request.session.get('uid')
        user = Administrators.objects.filter(id=uid)[0]
        goods = Goods.objects.filter(administrator_id=user.id)
        return render(request, 'C_选择商品.html', locals())


# 接受 商品
def recv_goods(request):
    goods = request.GET.get('a')
    DIC['goods']=goods
    return HttpResponse('OK')


# 接受 购买人
def recv_people(request):
    people = request.GET.get('b')
    DIC['people']=people
    return HttpResponse('OK')


GOODS_PEOPLE_DIC = {
    'goods': '',
    'people': '',
}
BUY_PEOPLE_id = []


# 生成订单编号
def bianhao():
    bianhao = str(datetime.datetime.now())
    bianhao = bianhao.split()
    bianhao1 = bianhao[0].split('-')
    bianhao2 = bianhao[1].split(':')
    bianhao3 = bianhao2[2].split('.')
    bianhao = bianhao1+bianhao2[0:2]+bianhao3
    x = ''
    for i in bianhao:
        x+=i
    return x


# 添加订单页面
def add_order(request):
    if request.method == 'GET':
        try:
            if 'uid' in request.session:
                check = request.GET.get('check')
                uid = request.session.get('uid')
                user = Administrators.objects.filter(id=uid)[0]
                goods_id = eval(DIC.get('goods', ''))
                # 所选商品列表
                goods_lst = []
                for i in goods_id:
                    i = int(i)
                    good = Goods.objects.get(id=i)
                    goods_lst.append(good)

                    if int(good.goods_kucun) == 0:
                        return HttpResponse(good.goods_name+'库存为0请重新选择')

                GOODS_PEOPLE_DIC['goods'] = goods_lst
                if check:
                    BUY_PEOPLE_id.append(check)
                    people = Buy_peoples.objects.get(id=check)
                    return render(request, 'C_积分订单.html', locals())
                else:

                    # 购买人信息

                    people_id = int(DIC['people'])

                    people = Buy_peoples.objects.get(id=people_id)
                    GOODS_PEOPLE_DIC['people'] = people
                    print(people)
                    return render(request, 'C_添加订单.html', locals())
        except:
            return HttpResponse('未选择商品或者是购买人')



def add_order_2(request):
    if 'uid' in request.session:
        try:
            uid = request.session.get('uid')
            user = Administrators.objects.filter(id=uid)[0]
            goods = GOODS_PEOPLE_DIC['goods']
            x = request.GET.get('count_lst')
            x = x[:-31]
            x = x+']'
            shangpin_jianshu_lst = eval(x)
            sum_shangpin = request.GET.get('sp_count')
            youhui_top = float(request.GET.get('youhui_top')[1:])
            youhui = float(request.GET.get('youhui'))
            youhui_after = float(request.GET.get('youhui_after')[1:])
            select = request.GET.get('select')


            # 订单获得积分
            suohuojifen = float(int(youhui_after))*float(user.administrator_jifen)

            # 存订单
            order = Order(
                administrator_id=user,
                order_id=bianhao(),
                buy_prople=GOODS_PEOPLE_DIC['people'],
                chengjiao_money=youhui_top,
                youhuijine=youhui,
                chengjiao_allmoney=youhui_after,
                goumailiang=sum_shangpin,
                huodejifen=suohuojifen,
                zhifufangshi=select,
            )
            order.save()

            # 存商品

            index = 0
            for i in shangpin_jianshu_lst:
                # 修改商品信息 库存 销量
                good = goods[index]
                if good.goods_kucun == int(0):
                    return HttpResponse(json.dumps({'msg':good.goods_name+'库存为零,请重新选择'}))
                good.goods_xiaoliang = int(good.goods_xiaoliang)+int(i)
                good.goods_kucun = int(good.goods_kucun)-int(i)
                good.save()


                cart = Cart(
                    goods_id=goods[index],
                    order_id=order,
                    count=i,
                )
                index+=1
                cart.save()

            # 修改购买人信息
            people = GOODS_PEOPLE_DIC['people']
            people.buy_people_alljifen = suohuojifen+float(people.buy_people_alljifen)
            people.buy_people_keyongjifen = suohuojifen+float(people.buy_people_keyongjifen)
            people.buy_people_allmoney = youhui_after+float(people.buy_people_allmoney)

            people.save()

            return HttpResponse(json.dumps({'status':1, 'msg': '保存成功'}))
        except:
            return HttpResponse('请重新选择商品和购买人')


# 添加积分订单
def add_order_jifen(request):
    if 'uid' in request.session:
        # try:
        uid = request.session.get('uid')
        user = Administrators.objects.filter(id=uid)[0]
        goods = GOODS_PEOPLE_DIC['goods']
        for i in BUY_PEOPLE_id:
            buy_people = Buy_peoples.objects.get(id=i)
        x = request.GET.get('count_lst')
        x = x[:-31]
        x = x+']'
        shangpin_jianshu_lst = eval(x)
        sum_shangpin = request.GET.get('sp_count')
        xiaohaojifen = float(request.GET.get('youhui_top')[1:])
        select = request.GET.get('select')
        # print(shangpin_jianshu_lst, sum_shangpin, xiaohaojifen, buy_people)

        # 存订单
        order = Order(
            administrator_id=user,
            order_id=bianhao(),
            buy_prople=buy_people,
            xiaohaojifen=xiaohaojifen,
            goumailiang=sum_shangpin,
            zhifufangshi=select,
        )
        order.save()

        # 修改购买人信息
        if float(buy_people.buy_people_keyongjifen) < xiaohaojifen:
            print('asdsa')
            return HttpResponse(json.dumps({'msg':'积分不足'}))
        else:
            buy_people.buy_people_keyongjifen = float(buy_people.buy_people_keyongjifen) - xiaohaojifen

            buy_people.save()


        # 存商品
        index = 0
        print(len(shangpin_jianshu_lst))
        print(goods)
        for i in shangpin_jianshu_lst:
            # 修改商品信息 库存 销量
            good = goods[index]
            if good.goods_kucun == int(0):
                return HttpResponse(json.dumps({'msg':good.goods_name+'库存为零,请重新选择'}))
            good.goods_xiaoliang = int(good.goods_xiaoliang)+int(i)
            good.goods_kucun = int(good.goods_kucun)-int(i)
            good.save()


            cart = Cart(
                goods_id=goods[index],
                order_id=order,
                count=i,
            )
            index+=1
            cart.save()



        return HttpResponse(json.dumps({'status':1, 'msg': '保存成功'}))
        # except:
        #     return HttpResponse('请重新选择商品和购买人')


# 删除单个订单
def del_order(request):
    order_id = request.GET.get('id')
    orders = Order.objects.get(id=order_id)
    if orders:
        orders.order_is_show = 0
        orders.save()
        return HttpResponse(json.dumps({'status': 1, 'msg': '删除成功'}))
    else:
        return HttpResponse(json.dumps({'status': 0, 'msg': '删除失败'}))




# 删除多个订单
def del_order_s(request):
    data = {'status': 1, 'msg': '删除成功'}
    data2 = {'status': 0, 'msg': '删除失败'}
    try:
        id = request.GET.get('id')
        print(id)
        orders = Order.objects.get(id=id)
        if orders:
            orders.order_is_show = 0
            orders.save()
            return HttpResponse(json.dumps(data))
        else:
            return HttpResponse(json.dumps(data2))
    except:
        return HttpResponse(json.dumps(data2))

# 查看订单详情
def order_xiangqing(request):
    if 'uid' in request.session:
        order_id = request.GET.get('order_id')
        order = Order.objects.get(id=order_id)
        cart_goods = Cart.objects.filter(order_id=order.id)

        return render(request, 'C_订单详情.html', locals())


# 查询
def select_order(request):
    if 'uid' in request.session:
        order_id = request.GET.get('order_id')
        people_name = request.GET.get('people_name')
        people_phone = request.GET.get('people_phone')
        order_date = request.GET.get('order_date')
        print(order_id, people_name, people_phone, order_date)

        uid = request.session.get('uid')
        user = Administrators.objects.filter(id=uid)[0]
        orders_top = Order.objects.filter(administrator_id=user.id).order_by('-id')
        # 所有的订单
        orders_all = []
        for i in orders_top:
            if i.order_is_show == 1:
                orders_all.append(i)

        orders = []

        if order_id and people_name and people_phone and order_date:
            for i in orders_all:
                if i.order_id == order_id and \
                        i.buy_prople.buy_people_phone == people_phone and \
                        i.buy_prople.buy_people_name == people_name and \
                        str(i.dingdanshijian).split()[0] == order_date:
                    orders.append(i)
            return render(request, 'C_订单管理.html', locals())

        if people_name and people_phone and order_date:
            for i in orders_all:
                if i.buy_prople.buy_people_phone == people_phone and \
                        i.buy_prople.buy_people_name == people_name and \
                        str(i.dingdanshijian).split()[0] == order_date:
                    orders.append(i)
            return render(request, 'C_订单管理.html', locals())

        if order_id and people_phone and order_date:
            for i in orders_all:
                if i.order_id == order_id and \
                        i.buy_prople.buy_people_phone == people_phone and \
                        str(i.dingdanshijian).split()[0] == order_date:
                    orders.append(i)
            return render(request, 'C_订单管理.html', locals())

        if order_id and people_name and order_date:
            for i in orders_all:
                if i.order_id == order_id and \
                        i.buy_prople.buy_people_name == people_name and \
                        str(i.dingdanshijian).split()[0] == order_date:
                    orders.append(i)
            return render(request, 'C_订单管理.html', locals())

        if order_id and people_name and people_phone:
            for i in orders_all:
                if i.order_id == order_id and \
                        i.buy_prople.buy_people_phone == people_phone and \
                        i.buy_prople.buy_people_name == people_name:
                    orders.append(i)
            return render(request, 'C_订单管理.html', locals())

        if order_id and people_name:
            for i in orders_all:
                if i.order_id == order_id and \
                        i.buy_prople.buy_people_name == people_name:
                    orders.append(i)
            return render(request, 'C_订单管理.html', locals())

        if order_id and people_phone:
            for i in orders_all:
                if i.order_id == order_id and \
                        i.buy_prople.buy_people_phone == people_phone:
                    orders.append(i)
            return render(request, 'C_订单管理.html', locals())

        if order_id and order_date:
            for i in orders_all:
                if i.order_id == order_id and \
                        str(i.dingdanshijian).split()[0] == order_date:
                    orders.append(i)
            return render(request, 'C_订单管理.html', locals())

        if people_name and people_phone:
            for i in orders_all:
                if i.buy_prople.buy_people_phone == people_phone and \
                        i.buy_prople.buy_people_name == people_name:
                    orders.append(i)
            return render(request, 'C_订单管理.html', locals())

        if people_name and order_date:
            for i in orders_all:
                if i.buy_prople.buy_people_name == people_name and \
                        str(i.dingdanshijian).split()[0] == order_date:
                    orders.append(i)
            return render(request, 'C_订单管理.html', locals())

        if people_phone and order_date:
            for i in orders_all:
                if i.buy_prople.buy_people_phone == people_phone and \
                        str(i.dingdanshijian).split()[0] == order_date:
                    orders.append(i)
            return render(request, 'C_订单管理.html', locals())

        if order_id:
            for i in orders_all:
                if i.order_id == order_id:
                    orders.append(i)
            return render(request, 'C_订单管理.html', locals())
        if people_name:
            for i in orders_all:
                if i.buy_prople.buy_people_name == people_name:
                    orders.append(i)
            return render(request, 'C_订单管理.html', locals())
        if people_phone:
            for i in orders_all:
                if i.buy_prople.buy_people_phone == people_phone:
                    orders.append(i)
            return render(request, 'C_订单管理.html', locals())
        if order_date:
            for i in orders_all:
                if str(i.dingdanshijian).split()[0] == order_date:
                    orders.append(i)
            return render(request, 'C_订单管理.html', locals())




