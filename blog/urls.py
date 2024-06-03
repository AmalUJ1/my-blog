# importing django routing libraries
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blog import views

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('register/', views.register, name='register'),
    path('read_me/', views.read_me, name='read_me'),
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<int:post_id>/', views.update_post, name='update_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('login/', views.custom_login, name='login'),
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('about/', views.about, name='about'),
    path('privacy/', views.privacy, name='privacy'),
    path('tos/', views.tos, name='tos'),
    path('posts/<slug:slug>/', views.post_detail, name='post_detail'),
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]