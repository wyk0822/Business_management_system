from .views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^type/', goods_types_views),
    url(r'^del-type/', del_type),
    url(r'^del-type_two/', del_type_two, name='del_type_two'),
    url(r'^add_type/', add_type, name='add_type'),
    url(r'^add_type_1/', add_type_1, name='add_type_1'),
    url(r'^update_type/', update_type, name='update_type'),
    url(r'^update_type_1/', update_type_1, name='update_type_1'),
]
