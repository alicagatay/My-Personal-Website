from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='Homepage'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('blogposts', views.post_list, name='post_list')
]
