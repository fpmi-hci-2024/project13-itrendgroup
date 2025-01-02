
from django.urls import path, register_converter
from . import views


urlpatterns = [
    path('', views.NewsMain.as_view(), name ='main'),
    path('about/', views.about, name='about'),
    path('addpost/', views.AddPost.as_view(), name='addpost'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.NewsCategory.as_view(), name='category'),
]