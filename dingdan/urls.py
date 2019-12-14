from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^show_order/', show_order, name='show_order'),
    url(r'^recv_people/', recv_people, name='recv_people'),
    url(r'^recv_goods/', recv_goods, name='recv_goods'),
    url(r'^select_peoples/', select_peoples, name='select_peoples'),
    url(r'^select_goods/', select_goods, name='select_goods'),
    url(r'^add_order/', add_order, name='add_order'),
    url(r'^add_order_2/', add_order_2, name='add_order_2'),
    url(r'^del_order/', del_order, name='del_order'),
    url(r'^del_order_s/', del_order_s, name='del_order_s'),
    url(r'^order_xiangqing/', order_xiangqing, name='order_xiangqing'),
    url(r'^add_order_jifen/', add_order_jifen, name='add_order_jifen'),
    url(r'^select_order/', select_order, name='select_order'),

]
