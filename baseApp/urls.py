from django.conf.urls import url
from django.contrib import admin
from baseApp import views #导入sign 应用views 文件

urlpatterns = [
    url(r'^$', views.index), #添加index/路径配置
]
# handler404 = views.page_not_found
# handler500=views.page_error




