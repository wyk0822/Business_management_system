from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^show_huiyuan/', show_huiyuan, name='show_huiyuan'),
    url(r'^add_huiyuan/', add_huiyuan, name='add_huiyuan'),
    url(r'^add_huiyuan_2/', add_huiyuan_2, name='add_huiyuan_2'),
    url(r'^del_huiyuan/', del_huiyuan, name='del_huiyuan'),
    url(r'^del_huiyuan_s/', del_huiyuan_s, name='del_huiyuan_s'),
    url(r'^change_huiyuan/', change_huiyuan, name='change_huiyuan'),
    url(r'^change_huiyuan_2/', change_huiyuan_2, name='change_huiyuan_2'),
    url(r'^select_huiyuan/', select_huiyuan, name='select_huiyuan'),
]