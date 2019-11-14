from django.urls import path
from .views import *
from django.contrib import admin


urlpatterns = [
	path('post/cat/<str:slug>/', category, name='posts_url'),
    path('', home_view, name='home_url'),
	#path('category/', category_view, name='category_url'),
	path('category/<str:slug>/', category_view, name='category_detail_url'),
	#path('forums/', forum_view, name='post_detail_url'),
]