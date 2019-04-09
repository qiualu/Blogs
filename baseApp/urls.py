from django.conf.urls import url
from django.contrib import admin
from baseApp import views #导入sign 应用views 文件

urlpatterns = [
    url(r'^$', views.index, name="home"), #添加index/路径配置
    url(r'^about/', views.about),
    url(r'^blog_post/', views.blog_post),
    url(r'^contact/', views.contact),
    url(r'^gallery/', views.gallery),
]
# handler404 = views.page_not_found
# handler500=views.page_error




