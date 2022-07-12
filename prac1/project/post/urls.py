
from django.urls import path
from post import views

app_name = 'post'

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('detail/<int:post_pk>', views.detail, name='detail'),
    path('edit/<int:post_pk>', views.edit, name='edit'),
    path('delete/<int:post_pk>', views.delete, name='delete'),
    # path('post/signup', views.signup, name='signup'),
    # path('post/login', views.login, name='login'),
    # path('post/logout', views.logout, name='logout'),
    ]