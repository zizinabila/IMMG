from django.urls  import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.PostList, name='home'),
    # url(r'^organization/$', views.PostOrganizationList, name='organization'),
    url(r'^post/new/$', views.PostCreate, name='post-new'),
    url(r'^post/user/(?P<username>[\w-]+)/$', views.PostUserList, name='post-user-list'),
    url(r'^post/category/(?P<slug>[\w-]+)/$', views.PostCategoryList, name='post-category-list'),
    url(r'^post/(?P<slug>[\w-]+)/$', views.PostDetail, name='post-detail'),
    # url(r'^admin/?P<slug>[\w-]+)/$', views.PostCreate, name='post-new'),
]
