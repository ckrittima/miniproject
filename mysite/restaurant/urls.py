from django.urls import path
from restaurant import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:restaurant_id>', views.detail, name='detail'),
    path('login/', views.my_login, name='login'),
    path('logout/', views.my_logout, name='logout')

]