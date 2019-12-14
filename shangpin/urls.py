from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', show_goods),
    url(r'^delgoods/', del_goods),
    url(r'^delgoods_two/', del_goods_two),
    url(r'^update_goods/', update_goods, name='update_goods'),
    url(r'^update_goods_2/', update_goods_2, name='update_goods_2'),
    url(r'^change_goods/', change_goods, name='change_goods'),
    url(r'^change_goods_2/', change_goods_2, name='change_goods_2'),


]
