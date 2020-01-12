from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from accounts import views
from django.contrib.auth.views import (
LoginView, LogoutView)

from django.urls import path

app_name='accounts'

urlpatterns = [
#path('', views.home, name="home"),
path('signup/', views.signup, name="signup"),
path('profile/', views.view_profile, name='view_profile'),  
path('login/', views.login, name="login"),
path('posts/', views.index),
path('top/', views.top),

#   path('', views.detail.as_view(), name='home'),


#url(r'^posts/(?P<post_id>\d+)/$', views.detail),
#path('add-post/', views.add_post),

path('celebs/', views.celebs),
url(r'^celebs/(?P<celebs_id>\d+)/$', views.celebs_detail),
url(r'^add-celebs/$', views.add_celebs),


url(r'^posts/(?P<post_id>\d+)/update/$', views.update, name='update'),

url(r'^posts/(?P<post_id>\d+)/comment/$', views.add_comment),

#url(r'^posts/(?P<post_id>\d+)/delete/$', views.delete),

]
