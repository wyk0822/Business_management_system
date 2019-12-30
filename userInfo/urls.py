from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/', login_view, name='login'),
    url(r'^register/', register_view, name='register'),
    url(r'^logout/', logout_views, name='logout'),
    url(r'^check_uphone/$', check_uphone_views),
    url(r'^settings/$', settings, name='settings'),
    url(r'^settings_2/$', settings_2, name='settings_2'),
    url(r'^update_pwd/$', update_pwd, name='update_pwd'),
    url(r'^update_security_img/$', update_security_img, name='update_security_img'),
    url(r'^forget_pwd/$', forget_pwd, name='forget_pwd'),
    url(r'^email_modfiy_pwd/$', email_modfiy_pwd, name='email_modfiy_pwd'),
    url(r'^test_html/$', test_html, name='test_html'),
]
