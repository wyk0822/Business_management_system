from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Administrators)
admin.site.register(Buy_peoples)
admin.site.register(Goods_types)
admin.site.register(Goods)
admin.site.register(Order)
admin.site.register(Cart)

