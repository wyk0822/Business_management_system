"""wx_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('shangpin.urls')),
    url(r'^userInfo/', include('userInfo.urls')),
    url(r'^dingdan/', include('dingdan.urls')),
    url(r'^leibie/', include('leibie.urls')),
    url(r'^huiyuan/', include('huiyuan.urls')),
    url(r'^captcha/', include('captcha.urls')),
]
# from django.conf import settings

# if settings.DEBUG is False:
#     urlpatterns += patterns('',
#         url(r'^static/(?P<path>.*)$', 'django.views.static.serve', { 'document_root': settings.STATIC_ROOT,
#         }),
#    )