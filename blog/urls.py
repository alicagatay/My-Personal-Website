from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='Homepage'),
    path('blog/post<int:pk>/', views.post_detail, name='post_detail'),
    path('blog', views.post_list, name='post_list'),
    path('about', views.aboutpage, name='about'),
    path('contact', views.contactpage, name='contact'),
    path('skills', views.skillspage, name='skills'),
    ]
