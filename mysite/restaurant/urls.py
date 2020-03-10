from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:restaurant_id>', views.detail, name='detail')
]