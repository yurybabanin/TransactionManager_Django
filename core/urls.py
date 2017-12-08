from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.post_list, name = 'post_list'),
    url(r'^show/(?P<id>\d+)/$', views.show_cur_tran, name='show'),
    url(r'^tran_new$', views.tran_new, name='tran_new')

]